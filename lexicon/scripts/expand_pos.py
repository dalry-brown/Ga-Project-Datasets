import csv
import re

# === Paste your abbreviation dictionary here ===
abbr_dict = {
    "adj": "adjective",
    "adv": "adverb",
    "ag": "agentive",
    "Ak": "Akan",
    "Ar": "Arabic",
    "arith": "arithmetic",
    "As": "Asante",
    "aux": "auxiliary",
    "Aw": "Awutu",
    "bibl": "biblical usage",
    "Braz": "Brazilian usage",
    "C": "Cansdale (source/author)",
    "colloq": "colloquial",
    "comp": "compare",
    "cpd": "compound",
    "conj": "conjunction",
    "cop": "copula",
    "D": "Dutch",
    "Da": "Dangme",
    "Dan": "Danish",
    "def": "definite",
    "dep": "dependent (of verbs)",
    "dem": "demonstrative",
    "descr": "descriptive of / describing",
    "det": "determiner",
    "dfct": "defective (of verbs)",
    "E": "Ewe",
    "EG": "Early Ga",
    "Ef": "Efutu",
    "egr": "egressive",
    "empl": "emphatic",
    "Eng": "English",
    "esp": "especially",
    "euph": "euphemism",
    "excl": "exclamation / interjection",
    "expn": "expression",
    "Fa": "Fante",
    "fem": "feminine",
    "fig": "figurative usage",
    "Fr": "French",
    "fut": "future",
    "ger": "gerund",
    "Ger": "German",
    "hab": "habitual aspect",
    "Hau": "Hausa",
    "id": "idem / the same",
    "imp": "imperative (mood)",
    "impert": "imperfective (aspect)",
    "incl": "including",
    "ingr": "ingressive",
    "intens": "intensifier",
    "intent": "intentive (aspect)",
    "invol": "involitional",
    "irreg": "irregular form",
    "iter": "iterative",
    "La": "Larteh",
    "loc": "locative",
    "n": "noun",
    "nn": "proper noun / noun (variant) # VERIFY",
    "neg": "negative",
    "neol": "neologism",
    "non-def": "non-definite",
    "O": "Obutu (personal name / source) # VERIFY",
    "obj": "object",
    "obsol": "obsolete",
    "obsolesc": "obsolescent",
    "opp": "opposite of",
    "P": "Protten (personal name / source) # VERIFY",
    "prt": "particle",
    "pejor": "pejorative",
    "perf": "perfect aspect",
    "pers": "person",
    "PGD": "Proto-Ga-Dangme",
    "pl": "plural",
    "P.L": "Philip Laryea (source) # VERIFY",
    "Port": "Portuguese",
    "pos": "positive",
    "poss": "possessive",
    "postpos": "postposition",
    "pred": "predicative",
    "pref": "prefix",
    "prep": "preposition",
    "prob": "probably",
    "prog": "progressive",
    "pron": "pronoun",
    "prov": "proverb",
    "provb": "proverbial / proverbial (alt) # VERIFY",
    "quant": "quantifier",
    "que": "question",
    "ref": "reference",
    "relig": "religious",
    "s": "singular",
    "sbjv": "subjunctive (mood)",
    "subj": "subject",
    "sp": "species",
    "Span": "Spanish",
    "sth": "something",
    "suff": "suffix",
    "syn": "synonym",
    "ult": "ultimately derived from",
    "usu": "usually",
    "v": "verb",
    "var": "variant of",
    "vbid": "verb variant / verb id (see source) # VERIFY",
    "volit": "volitional",
    "Z": "Zimmermann (source) # VERIFY",
}

# === Functions ===

def normalize_token(token: str) -> str:
    """Normalize abbreviation token (strip spaces, trailing dot, case)."""
    return token.strip().rstrip('.')

def expand_field(field: str) -> str:
    """Expand part_of_speech field using abbr_dict. Handles multiple tags."""
    if not field:
        return field
    # split by common separators
    tokens = re.split(r'[;,/| ]+', field)
    expanded = []
    for tok in tokens:
        if tok == "":
            continue
        norm = normalize_token(tok)
        if norm in abbr_dict:
            expanded.append(abbr_dict[norm])
        else:
            expanded.append(norm)  # keep unknown as-is
    # remove duplicates while preserving order
    seen, result = set(), []
    for item in expanded:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return ", ".join(result)

# === Main script ===
def expand_csv(input_file: str, output_file: str):
    with open(input_file, newline='', encoding="utf-8") as inf, \
         open(output_file, "w", newline='', encoding="utf-8") as outf:
        reader = csv.reader(inf)
        writer = csv.writer(outf)

        header = next(reader, None)
        if header:
            writer.writerow(header)

        for row in reader:
            if len(row) >= 4:
                row[3] = expand_field(row[3])
            writer.writerow(row)

    print(f"✅ Expanded file saved as: {output_file}")

# Example usage:
expand_csv("dataset.csv", "dataset_expanded.csv")
