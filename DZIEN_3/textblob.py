#przykłdowe opinie
opinions = [
    "This product is amazing and exceeded my expectations!",
    "I think and I suppose that this product is quite qood and I think that exceeded my expectations!",
    "I am disappointed with the quality and will not recommend it.",
    "The service was okay, but it could be much better.",
    "Big Shit!",
    "Beautiful disaster!"
]


#analiza sentymentu
for opinion in opinions:
    blob = TextBlob(opinion)
    sentiment = blob.sentiment
    print(f"\nTekst: {opinion}")
    print(f"polaryzcja: {sentiment.polarity:.2f} (od -1 do 1, gdzie 1 to pozytywny teskt a -1 negatywny)")
    print(f"subiektywnośc: {sentiment.subjectivity:.2f} (od 0 do 1, gdzie 1 to subiektywny teskt a 0 niesubiektywny)\n")
    print("_"*50)
