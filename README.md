# Dissertation-IAS-MSc

"Linguistic Alignment in Social Media: Detecting Alignment of Twitter Conversation Features Through Various Measures" 

Because it is against Twitter’s terms of service to publish tweet text or any identifying information about individual users, the data used in generating the report has not been shared. Cell outputs from Jupyter Notebooks used in computation and analysis have been cleared to maintain Twitter user privacy. 


**Jupyter Notebooks:** 

| File | Content |
| ------------- | ------------- |
| ImportCSV_ExploratoryAnalysis.ipynb  | Reads the raw csv file of twitter data into a data frame and explores properties of that data (eg. Frequency of individual user tweets, time of day, gap between tweet and reply). |
| Tokenize_Tag_Tweets.ipynb  | Isolates raw twitter data tweet and reply messages, cleans them, tokenises them with the TweetNLP Twokenizer python port (https://github.com/myleott/ark-twokenize-py) and feeds them into the CMU TweetNLP Tagger (https://github.com/brendano/ark-tweet-nlp). These items require downloading from GitHub - the jar files required to implement them were not included in this code set. |
| SCP_Coh_PosBigrams.ipynb| Get Subtractive Conditional Probability (SCP) Cohesion scores and visualizations for POS tags and bigrams. | 
|SCP_Accom_Pos.ipynb|Get Subtractive Conditional Probability (SCP) Accommodation scores and visualizations for POS tags. Also contains code for conducting a two-tailed paired t-test on probability estimates. |
|SCP_Accom_BigramsStats.ipynb|This notebook generates SCP Accommodation scores for bigrams, in addition to applying Fisher’s Exact test to pos tags and a two tailed t-test to bigrams to verify results. |
|LSM_PosBigrams.ipynb|Gets the Linguistic Style Matching scores for POS tags and Bigrams isolated from the tagged tweets dataset. |
|LLA_PosBigrams.ipynb|Generates Local Linguistic Alignment scores for Pos tags and Bigrams isolated from the tagged tweets datasets. |
|LLR_PosBigrams.ipynb|Generates log likelihood ratio scores for POS tags and Bigrams isolated from the tagged tweets dataset. Includes investigation of feature frequencies to determine alignment or disalignment. |
|Afinn_SCP_LSM_LLR.ipynb|Generates scores for all measures using Afinn sentiment tags as features (https://pypi.org/project/afinn/). |
|NRC_SCP_LSM_LLR_Stats.ipynb|Generates emotion counts for tweet tokens using the NRC Hashtag Emotion Lexicon (http://saifmohammad.com/WebPages/AccessResource.htm), turns those into binary markers, and inputs those as features into all measures. Contains statistical tests (t-test, fisher’s exact). |


**Python Files:**

| File | Content |
|------|----------|
|BigramCode.py|Contains functions relevant to creating and cleaning bigrams from tweet tags. |
|FunctionsForLLR.py|Contains functions to perform log likelihood ratio measure. |
|NRCHash.py|Contains functions to perform accommodation measures on the NRC Hashtag Emotion lexicon alignment markers.|
|	SCP_Code.py|Contains functions to perform SCP cohesion estimations on data. |

