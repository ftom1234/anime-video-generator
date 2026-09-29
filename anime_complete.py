#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anime Video Generator - Professional Cinematic Anime Scene
مشروع مولد فيديو أنمي احترافي مع مؤثرات سينمائية

Features:
- Professional color grading (dark luxury palette)
- Cinematic transitions and camera movements
- Particle effects (snow, light, glow)
- Sound effects generation
- Character animation with dynamic poses
- Multi-layer background with depth
- Custom anime opening sequence

Author: Copilot Anime Studio
Version: 1.0.0
"""

from manim import *
import numpy as np
import random
import math
import wave
import struct
from pathlib import Path


# ============================================================================
# AUDIO EFFECTS GENERATION
# ============================================================================

class AudioEffectGenerator:
    """Generate cinematic sound effects for anime scenes"""

    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    @staticmethod
    def sine_wave(frequency, duration, sample_rate=44100, volume=0.35):
        """Generate pure sine wave"""
        samples = int(sample_rate * duration)
        times = np.linspace(0, duration, samples, endpoint=False)
        wave_data = volume * np.sin(2 * np.pi * frequency * times)
        return wave_data.astype(np.float32)

    @staticmethod
    def add_noise(data, amount=0.03):
        """Add noise to signal"""
        noise = np.random.normal(0, amount, data.shape)
        return data + noise

    @staticmethod
    def save_wav(path, samples, sample_rate=44100):
        """Save numpy array as WAV file"""
        # Normalize
        if np.max(np.abs(samples)) > 0:
            scaled = np.int16(samples / np.max(np.abs(samples)) * 32767 * 0.9)
        else:
            scaled = np.int16(samples)

        with wave.open(path, 'wb') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            for s in scaled:
                wav_file.writeframes(struct.pack('<h', int(s)))

    def generate_swish(self, filename='sfx_swish.wav'):
        """Cinematic swish/whoosh sound"""
        swish = self.sine_wave(900, 0.2) + self.sine_wave(1300, 0.2, volume=0.2)
        swish = self.add_noise(swish, 0.04)
        self.save_wav(filename, swish, self.sample_rate)
        print(f"✓ Generated: {filename}")

    def generate_flash(self, filename='sfx_flash.wav'):
        """Bright flash/impact sound"""
        flash = self.sine_wave(250, 0.3) + self.sine_wave(150, 0.3, volume=0.25)
        flash = self.add_noise(flash, 0.06)
        self.save_wav(filename, flash, self.sample_rate)
        print(f"✓ Generated: {filename}")

    def generate_ambience(self, filename='sfx_ambience.wav'):
        """Dark atmospheric ambience"""
        ambience = np.zeros(int(self.sample_rate * 2.0))
        for f in [45, 60, 80, 120]:
            ambience += self.sine_wave(f, 2.0, volume=0.07)
        ambience = self.add_noise(ambience, 0.02)
        self.save_wav(filename, ambience, self.sample_rate)
        print(f"✓ Generated: {filename}")

    def generate_transition(self, filename='sfx_transition.wav'):
        """Cinematic transition sound"""
        freq_start = 200
        freq_end = 800
        duration = 0.5
        samples = int(self.sample_rate * duration)
        times = np.linspace(0, duration, samples, endpoint=False)
        
        freq_sweep = np.linspace(freq_start, freq_end, samples)
        transition = np.sin(2 * np.pi * freq_sweep * times / duration)
        transition = transition * (1 - times / duration)  # Fade out
        transition = self.add_noise(transition, 0.05)
        
        self.save_wav(filename, transition, self.sample_rate)
        print(f"✓ Generated: {filename}")

    def generate_all(self):
        """Generate all sound effects"""
        print("\n" + "="*50)
        print("🎵 GENERATING SOUND EFFECTS")
        print("="*50)
        self.generate_swish()
        self.generate_flash()
        self.generate_ambience()
        self.generate_transition()
        print("="*50 + "\n")


# ============================================================================
# CHARACTER DESIGN COMPONENTS
# ============================================================================

class CharacterX:
    """Build the anime character 'X' with modular components"""

    @staticmethod
    def create_body():
        """Create main body torso"""
        body = RoundedRectangle(
            width=2.3,
            height=3.2,
            corner_radius=0.5,
            fill_color='#171d24',
            fill_opacity=1
        )
        body.set_stroke(color='#2f3b46', width=2)
        body.move_to(0.2 * DOWN)
        return body

    @staticmethod
    def create_head():
        """Create head shape"""
        head = Circle(radius=0.6, fill_color='#202d34', fill_opacity=1)
        head.move_to(1.15 * UP)
        head.set_stroke(width=0)
        return head

    @staticmethod
    def create_hair():
        """Create dynamic hair"""
        hair = Polygon(
            [-0.8, 0.8, 0],
            [0.0, 1.5, 0],
            [0.8, 0.8, 0],
            [0.55, 0.2, 0],
            [-0.55, 0.2, 0],
            fill_color='#060a0e',
            fill_opacity=1
        )
        hair.move_to(1.15 * UP)
        hair.set_stroke(width=0)
        return hair

    @staticmethod
    def create_mask():
        """Create face mask"""
        mask = Rectangle(
            width=0.9,
            height=0.45,
            fill_color='#020509',
            fill_opacity=1
        )
        mask.move_to(1.15 * UP)
        mask.set_stroke(width=0)
        return mask

    @staticmethod
    def create_face_mark():
        """Create X mark on face"""
        x_mark = VGroup(
            Line([-0.35, -0.4, 0], [-0.12, 0.4, 0], color=WHITE, stroke_width=7),
            Line([0.12, 0.4, 0], [0.35, -0.4, 0], color=WHITE, stroke_width=7)
        )
        x_mark.move_to(1.15 * UP)
        return x_mark

    @staticmethod
    def create_arms():
        """Create both arms"""
        arm_l = RoundedRectangle(
            width=0.55,
            height=1.5,
            corner_radius=0.2,
            fill_color='#121b23',
            fill_opacity=1
        )
        arm_l.rotate(-0.5)
        arm_l.move_to([-1.45, -0.1, 0])
        arm_l.set_stroke(width=0)

        arm_r = RoundedRectangle(
            width=0.55,
            height=1.5,
            corner_radius=0.2,
            fill_color='#121b23',
            fill_opacity=1
        )
        arm_r.rotate(0.5)
        arm_r.move_to([1.45, -0.1, 0])
        arm_r.set_stroke(width=0)

        return VGroup(arm_l, arm_r)

    @staticmethod
    def create_legs():
        """Create both legs"""
        leg_l = RoundedRectangle(
            width=0.72,
            height=1.8,
            corner_radius=0.2,
            fill_color='#0b1318',
            fill_opacity=1
        )
        leg_l.move_to([-0.5, -2.7, 0])
        leg_l.set_stroke(width=0)

        leg_r = RoundedRectangle(
            width=0.72,
            height=1.8,
            corner_radius=0.2,
            fill_color='#0b1318',
            fill_opacity=1
        )
        leg_r.move_to([0.5, -2.7, 0])
        leg_r.set_stroke(width=0)

        return VGroup(leg_l, leg_r)

    @staticmethod
    def create_chest_x():
        """Create X emblem on chest"""
        chest_x = VGroup(
            Line([-0.55, -0.5, 0], [-0.12, 0.55, 0], color=WHITE, stroke_width=12),
            Line([0.12, 0.55, 0], [0.55, -0.5, 0], color=WHITE, stroke_width=12)
        )
        chest_x.move_to(0.3 * UP)
        return chest_x

    @staticmethod
    def create_collar():
        """Create red collar accent"""
        collar = ArcBetweenPoints(
            LEFT * 0.7 + UP * 0.2,
            RIGHT * 0.7 + UP * 0.2,
            angle=PI
        )
        collar.set_stroke(color='#ff2d2d', width=10)
        collar.move_to(0.55 * UP)
        return collar

    @staticmethod
    def create_full_character():
        """Assemble complete character"""
        char = VGroup(
            CharacterX.create_body(),
            CharacterX.create_head(),
            CharacterX.create_hair(),
            CharacterX.create_mask(),
            CharacterX.create_face_mark(),
            CharacterX.create_arms(),
            CharacterX.create_legs(),
            CharacterX.create_chest_x(),
            CharacterX.create_collar()
        )
        char.scale(1.2)
        char.move_to(0.2 * DOWN)
        return char


# ============================================================================
# BACKGROUND & ENVIRONMENT
# ============================================================================

class CityBackground:
    """Generate procedural city skyline"""

    @staticmethod
    def create_skyline():
        """Create city buildings with windows"""
        skyline = VGroup()

        for i in range(15):
            width = 0.7 + random.random() * 0.9
            height = 1.8 + random.random() * 3.5

            building = Rectangle(
                width=width,
                height=height,
                fill_color='#0d1822',
                fill_opacity=1
            )
            building.set_stroke(width=0)
            building.move_to((i * 0.9 - 6.0, -2.6 + height / 2, 0))
            skyline.add(building)

            # Windows with random lights
            for y in range(4, int(height), 2):
                for x in range(0, int(width) - 1, 1):
                    if random.random() > 0.45:
                        window = Rectangle(
                            width=0.12,
                            height=0.12,
                            fill_color='#d5ecff',
                            fill_opacity=0.9
                        )
                        window.set_stroke(width=0)
                        offset = building.get_center() + np.array([
                            x * 0.18 - width / 2 + 0.12,
                            y * 0.22 - height / 2 + 0.15,
                            0
                        ])
                        window.move_to(offset)
                        skyline.add(window)

        return skyline

    @staticmethod
    def create_snow_particles(count=90):
        """Create falling snow particles"""
        flakes = VGroup()
        for _ in range(count):
            flake = Dot(radius=0.04, color=WHITE)
            flake.move_to([
                random.uniform(-7, 7),
                random.uniform(-3.5, 4),
                0
            ])
            flakes.add(flake)
        return flakes

    @staticmethod
    def create_glow_effect():
        """Create atmospheric glow"""
        glow = Circle(
            radius=2.0,
            fill_color='#17345c',
            fill_opacity=0.2
        )
        glow.move_to(0.5 * UP + 0.2 * LEFT)
        glow.set_stroke(width=0)
        return glow


# ============================================================================
# MAIN ANIME SCENE
# ============================================================================

class AnimeOpening(Scene):
    """Professional anime opening scene with all effects"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.camera.background_color = '#030b14'

    def construct(self):
        """Build the complete scene"""
        print("\n" + "="*50)
        print("🎬 CONSTRUCTING ANIME SCENE")
        print("="*50 + "\n")

        # === BACKGROUND ===
        print("Step 1: Building background...")
        bg = FullScreenRectangle(fill_color='#030b14', fill_opacity=1)
        bg.set_stroke(width=0)
        self.add(bg)

        # === LIGHTING ===
        print("Step 2: Adding glow effects...")
        glow = CityBackground.create_glow_effect()
        self.add(glow)

        # === CITY ===
        print("Step 3: Building city skyline...")
        skyline = CityBackground.create_skyline()
        self.play(FadeIn(skyline, shift=DOWN, run_time=2))

        # === SNOW ===
        print("Step 4: Adding snow particles...")
        flakes = CityBackground.create_snow_particles(90)
        self.add(flakes)

        # === CHARACTER ===
        print("Step 5: Rendering character...")
        character = CharacterX.create_full_character()
        self.play(FadeIn(character, run_time=1.8))

        # === TITLE ===
        print("Step 6: Adding title...")
        title = Text(
            "X: THE AWAKENING",
            font_size=42,
            color=WHITE,
            weight="BOLD"
        )
        title.to_edge(DOWN, buff=0.8)
        self.play(Write(title, run_time=2))

        # === CINEMATIC EFFECTS ===
        print("Step 7: Applying cinematic effects...")

        # Camera zoom
        self.play(
            self.camera.animate.set_zoom(1.08),
            run_time=2
        )

        # Camera pan
        self.play(
            self.camera.animate.frame_center.shift(UP * 0.25),
            run_time=2
        )

        # Snow animation
        print("Step 8: Animating particles...")
        self.play(
            *[
                flake.animate.shift(
                    UP * random.uniform(0.08, 0.3) +
                    LEFT * random.uniform(-0.08, 0.08)
                )
                for flake in flakes
            ],
            run_time=4,
            lag_ratio=0.02,
        )

        print("Step 9: Finalization...")
        self.wait(2)
        print("\n" + "="*50)
        print("✓ SCENE COMPLETE")
        print("="*50 + "\n")


# ============================================================================
# ADVANCED SCENES (OPTIONAL)
# ============================================================================

class ActionSequence(Scene):
    """Advanced action scene with multiple characters and effects"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.camera.background_color = '#0a0e14'

    def construct(self):
        """Build action sequence"""
        print("\n🎬 ACTION SEQUENCE STARTING...\n")

        # Background
        bg = FullScreenRectangle(fill_color='#0a0e14', fill_opacity=1)
        bg.set_stroke(width=0)
        self.add(bg)

        # Multiple glow layers
        glow1 = Circle(radius=2.5, fill_color='#1a3a5c', fill_opacity=0.15)
        glow1.move_to(2 * UP)
        glow2 = Circle(radius=2.0, fill_color='#8b0000', fill_opacity=0.1)
        glow2.move_to(2 * DOWN)
        self.add(glow1, glow2)

        # City
        skyline = CityBackground.create_skyline()
        self.add(skyline)

        # Main character
        main_char = CharacterX.create_full_character()
        self.play(FadeIn(main_char, run_time=1.5))

        # Action animation
        self.play(main_char.animate.shift(RIGHT * 2), run_time=1)
        self.play(
            main_char.animate.rotate(PI / 4),
            run_time=1
        )
        self.play(main_char.animate.scale(1.1), run_time=0.8)

        # Text overlay
        action_text = Text(
            "INITIATING COMBAT MODE",
            font_size=28,
            color='#ff2d2d'
        )
        action_text.to_corner(UR, buff=0.5)
        self.play(FadeIn(action_text, run_time=1))

        # Flash effect
        flash = FullScreenRectangle(fill_color=WHITE, fill_opacity=0.3)
        self.play(FadeIn(flash, run_time=0.2), FadeOut(flash, run_time=0.3))

        self.wait(1)


# ============================================================================
# CONFIGURATION & RENDERING
# ============================================================================

class AnimeConfig:
    """Configuration for rendering settings"""

    # Rendering quality presets
    QUALITY_LOW = {
        'pixel_height': 720,
        'frame_rate': 24,
        'quality': 'l',  # low
    }

    QUALITY_MEDIUM = {
        'pixel_height': 1080,
        'frame_rate': 30,
        'quality': 'm',  # medium
    }

    QUALITY_HIGH = {
        'pixel_height': 1440,
        'frame_rate': 60,
        'quality': 'h',  # high
    }

    QUALITY_4K = {
        'pixel_height': 2160,
        'frame_rate': 60,
        'quality': 'p',  # production
    }


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print(" 🎨 ANIME VIDEO GENERATOR - Professional Edition")
    print(" Version: 1.0.0")
    print("="*60)

    # Generate sound effects
    audio_gen = AudioEffectGenerator()
    audio_gen.generate_all()

    print("\n" + "="*60)
    print(" RENDERING OPTIONS:")
    print("="*60)
    print("""
    To render the opening scene, use one of these commands:

    LOW QUALITY (Fast):
    $ manim -ql anime_complete.py AnimeOpening

    MEDIUM QUALITY (Balanced):
    $ manim -qm anime_complete.py AnimeOpening

    HIGH QUALITY (Slow but beautiful):
    $ manim -qh anime_complete.py AnimeOpening

    PRODUCTION (4K Ultra):
    $ manim -qp anime_complete.py AnimeOpening

    WITH PREVIEW:
    $ manim -pql anime_complete.py AnimeOpening

    ACTION SEQUENCE:
    $ manim -pql anime_complete.py ActionSequence

    SAVE TO FILE:
    $ manim -ql anime_complete.py AnimeOpening -o output.mp4
    """)
    print("="*60 + "\n")

    # Optional: Direct scene construction for testing
    # Uncomment below to test locally
    # scene = AnimeOpening()
    # scene.render()
