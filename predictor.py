import pandas as pd
import numpy as np
import random


def get_predictions(user_input):
    diseases = [
        "Dengue", "Chikungunya", "COVID-19", "Malaria", "Typhoid", "Influenza"
    ]
    regions = [
        "Andhra Pradesh", "Telangana", "Kerala", "Karnataka", "Tamil Nadu"
    ]

    data = {
        "Region": [],
        "Disease": [],
        "Outbreak Likelihood (%)": []
    }

    for region in regions:
        sampled_diseases = random.sample(diseases, k=3)
        for disease in sampled_diseases:
            data["Region"].append(region)
            data["Disease"].append(disease)
            data["Outbreak Likelihood (%)"].append(random.randint(10, 95))

    df = pd.DataFrame(data)
    return df
