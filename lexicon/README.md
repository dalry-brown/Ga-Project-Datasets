# Ga Lexicon Dataset

A structured **lexical resource** for the Ga language, containing words, phonemic transcriptions (with tones), English meanings, and part-of-speech (POS) tags. This dataset is designed to support **computational linguistics, NLP applications, speech technology, and language preservation**.

---

## ✨ Introduction
The **Ga Lexicon Dataset** was developed to provide a machine-readable dictionary for the Ga language.  

**Goals:**
- Enable **speech recognition** and **speech synthesis** research through phoneme-level representations.  
- Support **morphological analysis** and **POS tagging** for Ga.  
- Contribute to the **digital preservation** of Ga, an under-resourced West African language.  
- Provide a **reference lexicon** for educational and linguistic use.  

---

## 📚 Data Source
- **Primary Resource:** *Ga–English Dictionary* by Mary Esther Kropp Dakubu.  

The dictionary contained all required linguistic information:  
- Ga words  
- Phonemic transcriptions (with tonal markers)  
- English meanings  
- Part-of-speech annotations  

---

## 🛠 Data Preparation

### 1. Manual Digitization
- The dictionary was **not available in digital form**.  
- Over **9,000 entries** were manually transcribed into a structured format.  
- Each entry includes:  
  - **Word** (Ga)  
  - **Phoneme representation** (with tone markings)  
  - **English meaning**  
  - **Part of Speech (POS)**  

### 2. Handling Tonal and Orthographic Features
- Ga is a **tonal language**, so tone markings were carefully preserved in the phoneme field.  
- Special Ga characters were transcribed using the **IPA typing tool** (https://ipa.typeit.org) to ensure phonetic accuracy.  

### 3. Data Structuring
- Final dataset organized into **CSV format** with schema:  

    word, phoneme, meaning, part_of_speech  

- **Sample entries:**

    | Word    | Phoneme              | Meaning                    | Part of Speech |
    |---------|----------------------|----------------------------|----------------|
    | aabateŋ | à à b à t é ŋ̀   | pig-in-the-middle game     | noun           |
    | aabia   | à à b í á        | canna lily                 | noun           |
    | ahabia  | à h à b í á      | canna lily                 | noun           |
    | aadɔŋ   | á à d ɔ́ ŋ́        | plum                       | noun           |
    | aaglɛmi | á à g l̀ ɛ̀ m í   | a wild fruit               | noun           |

---

## 📂 Folder Structure
    Ga_Lexicon_Dataset/
    ├── dataset.csv     # Full lexicon (word, phoneme, meaning, POS)
    └── README.md       # Documentation

---

## 🚀 Applications
- Training **speech recognition systems** by mapping Ga words to phoneme-level pronunciations.  
- Supporting **text-to-speech (TTS)** synthesis through phonemic input.  
- Enabling **morphological analysis** and **POS tagging** for Ga.  
- Providing a **digital dictionary** for linguistic and educational purposes.  

---

## 💻 Usage Example
    import pandas as pd

    # Load lexicon
    df = pd.read_csv("dataset.csv")

    # Preview first rows
    print(df.head())

    # Example: find all nouns
    nouns = df[df['part_of_speech'] == 'noun']
    print(nouns.sample(5))

---

## 👥 Authors
- **William Dalry Kpakpo Brown** (ID: 10952541)  
- **Jonathan Wilchield Arthur** (ID: 10945544)  
- **Michael Konadu** (ID: 10950757)  

---

## 📖 Citation
If you use this dataset, please cite as follows:

    @misc{ga_lexicon_dataset_2025,
      author       = {Brown, William Dalry Kpakpo and Arthur, Jonathan Wilchield and Konadu, Michael},
      title        = {Ga Lexicon Dataset},
      year         = {2025},
      howpublished = {https://github.com/dalry-brown/Ga-Project-Datasets},
      note         = {Digital lexicon of Ga words with phonemes, meanings, and POS annotations}
    }

---

## 📜 License
- **Code:** MIT License  
- **Dataset:** [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/)  

You are free to use, share, and adapt this dataset with attribution.

---
