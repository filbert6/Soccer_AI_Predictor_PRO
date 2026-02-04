from ml_models import *

def predict_match(match_data):
    # Placeholder Voting Ensemble simple
    main_score = "2-1"
    others = ["1-1", "2-0"]
    winner = match_data["home"]
    btts = "YES"
    ou = "Over 2.5"
    mtft = "X / 1"

    return {
        "main_score": main_score,
        "others": others,
        "winner": winner,
        "btts": btts,
        "over_under": ou,
        "mtft": mtft
    }
