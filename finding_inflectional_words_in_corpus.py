import re

# Sample data (based on the example provided)
# words_with_paradigms = {
#     'Pasala': {
#         'rAw/a__n': ['वेधन', 'वेधनें', 'वेधनों'],
#         'BIda/__n': ['वेधन'],
#         'Gar/a__n': ['वेधन', 'वेधनों'],
#         'Karc/a__n': ['वेधन', 'वेधने', 'वेधनों']
#     }
# }

# words_with_paradigms = {
#     "Pasala": {
#         "rAw/a__n": [
#             "फसलों",
#             "फसल",
#             "फसलें"
#         ],
#         "BIda/__n": [],
#         "Gar/a__n": [
#             "फसलों",
#             "फसल"
#         ],
#         "Karc/a__n": [
#             "फसलों",
#             "फसले",
#             "फसल"
#         ]
#     }
# }


# Function to find matches in corpus and determine best matching paradigm
def find_best_matching_paradigm(words_with_paradigms, corpus):
    # print(words_with_paradigms,'llllllllllllll')
    # Dictionary to store the paradigm with most matches for each base word
    best_paradigm_matches = {}

    for base_word, paradigms in words_with_paradigms.items():
        max_matches = 0
        best_paradigm = None

        # Iterate through each paradigm and its inflectional words
        for paradigm, words in paradigms.items():
            # Count matches in corpus for the current paradigm
            match_count = sum(1 for word in words if word in corpus)

            print(f"Inflectional words for base '{base_word}' using paradigm '{paradigm}':")
            print(f"Words in paradigm: {words}")
            print(f"Matching words in corpus: {[word for word in words if word in corpus]}")
            print(f"Match count: {match_count}")

            # Update the best matching paradigm if this has more matches
            if match_count > max_matches:
                max_matches = match_count
                best_paradigm = paradigm

        # Store the best paradigm for the base word
        best_paradigm_matches[base_word] = (best_paradigm, max_matches)

    return best_paradigm_matches

