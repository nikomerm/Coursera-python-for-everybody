from pathlib import Path

ROOT = Path("python-for-everybody")

# Όνομα φακέλου -> αριθμός εβδομάδων (άλλαξε τους αριθμούς αν χρειάζεται)
COURSES = {
    "01-getting-started": 6,
    "02-data-structures": 6,
    "03-web-data": 6,
    "04-databases": 6,
    "05-capstone": 0,
}

RESOURCE_FILES = ["cheatsheet.md", "mistakes-log.md", "glossary.md"]


def make_file(path, content=""):
    if not path.exists():  # δεν γράφει πάνω σε υπάρχοντα αρχεία
        path.write_text(content, encoding="utf-8")


for course, weeks in COURSES.items():
    (ROOT / course).mkdir(parents=True, exist_ok=True)
    for n in range(1, weeks + 1):
        week = ROOT / course / f"week-{n:02d}"
        (week / "exercises").mkdir(parents=True, exist_ok=True)
        make_file(week / "notes.md", f"# {course} - Week {n}\n\n## Τι έμαθα\n\n## Παράδειγμα κώδικα\n")

(ROOT / "_resources").mkdir(parents=True, exist_ok=True)
for name in RESOURCE_FILES:
    make_file(ROOT / "_resources" / name, f"# {name.replace('.md', '')}\n")

make_file(ROOT / "progress.md", "# Progress\n\n| Ημερομηνία | Ώρες | Τι ολοκληρώθηκε |\n|---|---|---|\n")

print("Έτοιμο!")
