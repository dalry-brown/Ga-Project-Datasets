# Ga Audio-Text Corpus

A structured parallel dataset of **Ga Bible verses** with aligned **audio recordings and transcriptions**, designed to support speech technology research and the preservation of the Ga language.

---

## ✨ Introduction
The **Ga Audio-Text Corpus** was created by aligning verses from the Ga Bible text with corresponding audio recordings.

**Goals:**
- Enable the development of **speech technologies** such as Text-to-Speech (TTS) and Automatic Speech Recognition (ASR).
- Provide resources for **linguistic research** on the Ga language.
- Contribute to the **digital preservation** of an under-resourced West African language.

---

## 📚 Data Sources
- **Text Source:** Ga Bible (Old Testament, ~10 chapters processed).  
- **Audio Source:** Ga Audio Bible (from https://live.bible.is/), provided as a compressed ZIP archive with book- and chapter-level recordings.

---

## 🛠 Data Preparation

### 1. Audio Structuring
- Extracted audio into book- and chapter-level recordings.  
- Example: `Genesis/Genesis_1.mp3`, `Genesis/Genesis_2.mp3`, etc.

### 2. Manual Segmentation
- Segmentation performed with **Audacity**.  
- Playback speed reduced for precision.  
- Verse boundaries marked in waveform/spectrogram view.  
- Labels exported in timestamp format:

    7.608263    7.608263    Verse 1  
    11.220365   11.220365   Verse 2

### 3. Automated Splitting
- Custom Python script used to split chapter audio into **verse-level `.wav` clips**.

### 4. Text Alignment
- Verse text collected and aligned to verse-level audio.  
- Example:

    Verse 1: Shishijee mli lɛ Nyɔŋmɔ bɔ ŋwɛi kɛ shikpɔŋ.  
    Verse 2: Ni shikpɔŋ lɛ yɛ olɛŋlɛ, ni efee flóŋŋ...

### 5. Dataset Assembly
- Final CSV metadata schema:

    audio_file, text, duration

- Example rows:

    output/verses/genesis/genesis_1_verse_1.wav,Shishijee mli lɛ Nyɔŋmɔ bɔ ŋwɛi kɛ shikpɔŋ.,3.61  
    output/verses/genesis/genesis_1_verse_2.wav,"Ni shikpɔŋ lɛ yɛ olɛŋlɛ, ni efee flóŋŋ...",11.14

---

## 📂 Folder Structure
    Ga_Bible_Project/
    ├── labels/             # Audacity label files (per chapter)
    │   ├── genesis/
    │   └── exodus/
    ├── original_audio/     # Original chapter-level audio
    │   ├── genesis/
    │   └── exodus/
    ├── output/verses/      # Verse-level segmented audio
    │   ├── genesis/
    │   └── exodus/
    ├── text/               # Verse-level transcriptions
    │   ├── genesis/
    │   └── exodus/
    └── dataset.csv         # Final metadata file

---

## ⬇️ Download
The full dataset (**≈2 GB**, audio + CSV) is available via Google Drive:

📦 https://drive.google.com/file/d/1pyHpDcc_vhXRZX9M7t_lj_c5_Q3H7mxC/view?usp=drive_link

---

## 🚀 Applications
- Training **Text-to-Speech (TTS)** systems  
- Training **Automatic Speech Recognition (ASR)** models  
- **Linguistic analysis** of the Ga language  
- **Digital preservation** of under-resourced languages

---

## 💻 Usage Example
    import pandas as pd

    # Load metadata
    df = pd.read_csv("dataset.csv")

    # Preview first rows
    print(df.head())

    # Example: loop through entries
    for audio_path, text in zip(df['audio_file'], df['text']):
        print(audio_path, "->", text)

---

## 👥 Authors
- **William Dalry Kpakpo Brown** (ID: 10952541)  
- **Jonathan Wilchield Arthur** (ID: 10945544)  
- **Michael Konadu** (ID: 10950757)

---

## 📖 Citation
If you use this dataset, please cite as follows:

    @misc{ga_audio_text_corpus_2025,
      author       = {Brown, William Dalry Kpakpo and Arthur, Jonathan Wilchield and Konadu, Michael},
      title        = {Ga Audio-Text Corpus},
      year         = {2025},
      howpublished = {https://github.com/dalry-brown/Ga-Project-Datasets},
      note         = {Ga language Bible verse audio-text dataset for speech technology research}
    }

---

## 📜 License
- **Code:** MIT License  
- **Dataset (audio + text):** [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

You are free to use, share, and adapt this dataset with attribution.

---
