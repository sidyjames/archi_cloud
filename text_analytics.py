from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "ad519f65cfdd4aa29b42687798eb7cf7"
endpoint = "https://textanalyticslab.cognitiveservices.azure.com/"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documents = [
    "Je suis très satisfait du service offert. Cela simplifie mon travail."
]

response = client.analyze_sentiment(documents)
for document in response:
    print(f"Sentiment: {document.sentiment}")

response = client.extract_key_phrases(documents)
for document in response:
    print(f"Phrases clés: {', '.join(document.key_phrases)}")
