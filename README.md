# Sentiment Analysis on Tokopedia TWS F9-5 Product Reviews

To fulfill natural language processing class' final assignment, we conducted sentiment analysis for TWS F9-5 product reviews on Tokopedia.
## Proposed Methodology
![Methodology](assets/nlp%20methodology.png)

## Data collection

We scraped data using **Selenium** library from **Tokopedia** [TWS F9-5](https://www.tokopedia.com/pinzyofficial/headset-bluetooth-tws-f9-5-led-smart-display-with-powerbank-f9-5/review) product rewiews. TWS F9-5 is an inexpensive TWS that only costs Rp34,000. Over 10,000 products were sold and 12,000 ratings were given, with an overall rating of 4.7. Unfortunately, out of the 12,000 ratings, only 4,500 reviews were provided. After scraping the data, we found **3,000 valid reviews** as the rest did not include any text.
<br>
<br>
Below are some sample text obtained from the scraping.

| Rating | Comment                                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------------------|
| 1      | barang gue ga sampe, bacaannya tunggu investigasi dari kurir, tiba" pelanggan tidak menindak lanjuti proses komplain |
| 4      | paket sesuai,,minus nya budeg sebelah, lampu indikator speaker kalo mati suara juga mati,ke senggol mati             |
| 5      | sesuai deskripsi,,barang bagus,murah tapi tidak murahan,,,cocok di hp redmi 10C                                      |

## Data Preprocessing
It is necessary to clean and preprocess the data before feeding them into the deep learning model with the hope of increasing its learning efficiency. The following steps are carried out for data preprocessing.

#### 1. Transform to lowercase and remove trailing whitespaces
This step ensures uniformity in text by converting all characters to lowercase, preventing variations that could effect model efficiency. While removing trailing whitespaces is essential for data cleanliness and preventing inconsistencies.

#### 2. Regex remover
Using regex, we **removed punctuation, special characters, digits, and emoji** so the text are streamlined to focus solely on their linguistic content.

#### 3. Spell correction
To make sure words are interpreted correctly, we performed a **manual spelling correction** by compiling all words into a dictionary, manually inspecting them, and mapping all the errors.

#### 4. Stemming
Reduces words to their base forms (e.g. balasan -> balas). In this step we used **Sastrawi**, a python library specialized to reduce inflected words in Indonesian Language (Bahasa Indonesia) to their base forms.

#### 5. Remove stopwords
Stopwords are common words that do not carry significant meaning in a given context thus can be omitted. (e.g. tidak, bukan, usah)

#### 6. Remove words that only contain 1 letter
We removed a handful instances of a singular letter that doesn't have any meaning or belongs to any words on the data.

## Data Annotation
In this project, the rating of the reviews determine their sentiment. Below are the rules:

>IF rating < 3 THEN sentiment = negative
<br>ELSE IF rating = 3 THEN sentiment = neutral
<br>ELSE IF rating > 3 THEN sentiment = positive

## Modelling
For this project we used **IndoBERT-base-p1** as the base model for the sentiment analysis model. IndoBERT is a state-of-the-art language model for Indonesian Langugage based on the BERT model. The pretrained model is trained using a masked language modeling (MLM) objective and next sentence prediction (NSP) objective.
