import os
from midiutil import MIDIFile
import random

def generate_midi_beat(beat_pattern, file_name):
    """Generate a MIDI file based on the given beat pattern."""
    midi = MIDIFile(1)
    midi.addTempo(track=0, time=0, tempo=130)

    beat_to_midi = {
        'K': 36,
        'S': 40,
        'H': 42,
        'O': 46,
        'P': 75,
        'Q': 76
    }

    time = 0
    for symbol in beat_pattern:
        if symbol in beat_to_midi:
            midi.addNote(track=0, channel=9, pitch=beat_to_midi[symbol], time=time, duration=8, volume=100)
        time += 1

    try:
        with open(file_name, "wb") as midi_file:
            midi.writeFile(midi_file)
    except PermissionError:
        print(f"Permission denied when trying to write to {file_name}.")
    except FileNotFoundError:
        print(f"Directory does not exist: {os.path.dirname(file_name)}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def randomize_beat(beat_pattern):
    """Semi-randomize elements of a beat pattern."""
    elements = list(beat_pattern)
    for i, symbol in enumerate(elements):
        if random.random() < 0.1:  # 10% chance to replace a symbol
            replacement = random.choice(['K', 'S', 'H', 'O', 'P', 'Q', '-'])
            elements[i] = replacement
    return ''.join(elements)

# Define some foundational future garage beat patterns
# base_patterns = [
#     "K-H-S-H-K-H-S-H",
#     "K-H-K-O-S--H-K-",
#     "K--S-H-K-H-S-O",
#     "K-H-S-O-K--S-H",
#     "K-O-S-H-K-O-S-H",
#     "K-H-S-H-K-S-H-S",
#     "K--S--K--S--K-",
#     "K-O-K-H-S-H-S-",
#     "K-H-K-H-K-H-K-H",
#     "K--S--O--H--K-",
#     "K-H-K-O-S-O-H-S",
#     "K--H--S--K--H-",
#     "K-H-S-H-S-K-H-S",
#     "K-O-K-O-K-O-S-H",
#     "K--S-H-K--S-H-",
#     "K-H-K-H-S-H-S-O",
#     "K-H-S--K-H-S-H-",
#     "K-O-K-H-K-O-K-H",
#     "K--S--K--H--S-",
#     "K-H-S-H-K--H--O",
#     "K-O-S--K-O-S-O",
#     "K-H-S-H-K-H--O-",
#     "K-H-K-O-K-H-K-O",
#     "K--S--K--S--H-",
#     "K-H-K-H-S--S--H",
#     "K--H--O--K--S-",
#     "K-H-S--K--S-H-",
#     "K-O-K-O-K--K--S",
#     "K--S--H-K-O-S-H",
#     "K-H-K--S-H-K-O-",
#     "K-H--O-K-H--O-S"
# ]

base_patterns = [
    "K-H-S-H-K-P-S-H",
    "K-H-K-P-S--H-Q-",
    "K-P-S-H-Q-H-S-O",
    "K-H-S-O-K-P-S-H",
    "K-O-S-H-K-Q-S-H",
    "K-H-S-H-P-S-H-Q",
    "K-Q-S--K-P-S--K",
    "K-O-K-H-S-Q-S-",
    "K-P-K-H-K-H-K-H",
    "K-Q-S--O-P-H--K",
    "K-H-K-O-P-O-H-S",
    "K--H-Q-S--K-P-H",
    "K-H-S-H-S-K-H-Q",
    "K-P-K-Q-K-O-S-H",
    "K-Q-S-H-K-P-S-H",
    "K-H-K-H-Q-H-S-O",
    "K-H-S-P-K-H-S-H-",
    "K-P-K-H-K-Q-K-H",
    "K--S-P-K--H-Q-S",
    "K-H-S-H-K-P-H--O",
    "K-P-S-P-K-O-S-O",
    "K-H-S-H-P-H--O-Q",
    "K-H-K-Q-K-H-K-P",
    "K-Q-S-P-K--S--H",
    "K-H-K-H-S-P-S-Q-H",
    "K-P-H--O-K-Q-S-",
    "K-H-S-P-K-P-S-H",
    "K-P-K-Q-K-P-K--S",
    "K-Q-S--H-K-P-S-H",
    "K-H-K-P-S-H-K-O-",
    "K-H--O-K-P--O-S"
]

# Extend the base patterns to 4 bars by repeating and randomizing
extended_patterns = []
for base_pattern in base_patterns:
    extended_pattern = base_pattern * 8
    for _ in range(2):  # Randomize 3 times for variation
        extended_pattern = randomize_beat(extended_pattern)
    extended_patterns.append(extended_pattern)

# Generate MIDI files for the extended patterns
for i, extended_pattern in enumerate(extended_patterns):
    file_name = f"beat_variant_{i+1}.mid"
    generate_midi_beat(extended_pattern, file_name)