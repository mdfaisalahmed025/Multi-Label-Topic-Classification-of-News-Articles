from config import KEYWORD_LABELS

def apply_weak_labels(text, labels):
   text = text.lower()
   label_set = set(labels)
   for label, keywords in KEYWORD_LABELS.items():
    if any(k in text for k in keywords):
       label_set.add(label)
       return list(label_set)