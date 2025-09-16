# PHARMASHIELD: Fake Drug Detection via Pharmacy Sales Analysis

## Project Overview  
PharmaShield is an unsupervised Machine learning-based detection system, designed to detect the distribution of fake drugs in Nigeria. This approach leverages an anomaly detection algorithm to spot irregularities in the retail supply of drugs, thereby providing a less costly, faster, scalable and proactive method to flag suspicious cases.  
## Project Background
Counterfeit and substandard drugs pose a serious health threat across African markets, take for example, Nigeria, where this problem is deeply rooted and dangerous. According to the National Agency for Food and Drug Administration and Control (NAFDAC), about 15-30% of medicines in circulation are counterfeit, most especially in rural and semi-urban markets where regulatory oversight is weaker due to the slow and ineffective traditional manual inspection techniques.
The usage of these drugs in consideration, may lead to:  
* Inefficiency of the drug against the use case  
* Harmful Side effects  
* Drug Resistance,  
Thereby, leading to an increased Morbidity and Mortality rate, Economic risks and loss of trust in the healthcare systems and in the ability of the institution to protect the interest of the concerned subjects.  
## Problem Statement  
The circulation of counterfeit drugs poses a critical threat to public health, supply chain integrity and trust in healthcare systems. Current detection methods used are traditional manual techniques, which are slow, not-scalable, costly and ineffective. There is, therefore, a need for a data-driven approach that can flag suspicious patterns in drug distribution and pricing, enabling earlier investigation and intervention.
## Objectives
### Primary Objective:  
To support regulatory agencies in reducing the circulation of counterfeit medicines in Nigeria by at least 10% within 24 months, through the development of a data-driven anomaly detection system that identifies suspicious patterns in drug distribution
### Secondary Objectives:  
* To ensure data quality and integrity.
* To generate insights on drug pricing and distribution across various brands, suppliers and pharmacies.
* To create relevant features that may signal counterfeit behaviour, and to train and evaluate anomaly detection algorithms to recognize and flag those behaviours.
* To integrate the model into a functional system for use by regulating agencies and continuous improvements  
## Data Understanding  
### Data Dictionary
Column Name	| Data Type	| Description
|-----|-----|-----|
Date	| Date |	Date when the sale occurred.
Pharmacy	| String	| Name of the pharmacy where the drug was sold.
Location	| String |	Whether the pharmacy is Urban or Rural.
Drug	| String |	Name of the drug (e.g., Amoxicillin, Artemisinin).
Brand	| String	| Brand name of the drug (may include unknown/fake brands).
Price	| Float	| Price per unit sold (in Naira ₦).
Quantity	| Integer	| Number of units sold in the transaction.
Supplier_Name	| String	| Supplier or distributor that provided the drug batch.
Batch_Number	| String	| Unique batch identifier assigned by supplier.
Expiry_Date	| Date	| Expiration date of the drug batch.
Sales_Channel	| String	| Channel where the sale was made (In-Store, Mobile Van, Market Stall).
Drug_Form	| String	| Form of the drug (Tablet, Syrup, Injection, etc.).

### Data Quality  
Data had quality issues such as:  
* Missing Values in columns such as Pharmacy, Drug, Brand, Supplier_Name, Price, and Quantity
* Inconsistencies in the name of the Drug Brands.  
### Data Cleaning  
* Missing values of Pharmacy name, Drug name, Brand and Supplier names could have been as a result of data entry errors or that there was actually no name for each of them, i.e., A drug without a brand name or a Pharmacy store buying from an unknown supplier. Removing them might cost the loss of data which is very important in the identification of counterfeit drugs and so they were filled with “Unknown”.
* Missing values in the Price column were not dropped. Instead, they were imputed using a brand-specific approach: for each drug, the missing price was replaced with the median price of that same drug within its corresponding brand. This will ensure that drug-brand consistency and the market pricing structure is preserved.
* Missing values in the Quantity column were also not dropped, but were instead imputed using a Pharmacy-Brand-Specific approach; for each drug, the missing quantity was replaced with the median quantity of that same drug, within its corresponding brand, bought by the same pharmacy, putting into consideration the brand-level pattern and pharmacy-specific purchasing behaviour.
* Among Brand Names, we noticed mis-spelled ones like MediPluz, Biokare, Hea1thFirst and FarmaTrust, and the first thought was to correct these to the correct brand names. But this also raised the idea that name irregularities in the Nigerian context, could be imitations of the original names and might be a counterfeit signal. So, they were left as they were.  
## Exploratory Data Analysis (EDA)
In order to uncover patterns in the data, we explored in three sections; Price distribution, Sales Volume and Brand Diversity.  
### Price Distribution
To understand the pricing patterns in our data, we began with a general exploration to understand the various statistical attributes of our data  
From there, we asked deeper questions, such as:  
* Do Prices vary across the urban and rural locations?
* Do Prices differ across the various drugs and their corresponding brands?
* What sales channel(s) is/are more associated with cheaper/more volatile pricing?
* Does the drug form affect the pricing of each drug? and so on.  
Location alone did not drive price differences as rural risks were probably more about distribution channels (market stalls, mobile vans) than pricing. But, the sales channels themselves showed balanced pricing, although traceability in informal outlets remains a risk. Mainstream brands (HealthFirst, Biocare, MediPlus, PharmaTrust) stayed within expected price ranges, while rare brands showed extreme highs or lows, signaling possible counterfeits.  
Other exploratory checks, such as prices by supplier, pharmacy, and expiry date, were also considered. These provided additional perspective but showed weaker influence on overall price variation.  
<img width="462" height="347" alt="image" src="https://github.com/user-attachments/assets/b9a4dbfa-e969-4921-836d-b3af50b1b6df" /><img width="499" height="347" alt="image" src="https://github.com/user-attachments/assets/78fc3402-8e23-4464-a8f1-9fc00180f3df" /><img width="462" height="334" alt="image" src="https://github.com/user-attachments/assets/b4ed5e19-b4e0-4896-8891-8d8250692a47" /><img width="499" height="334" alt="image" src="https://github.com/user-attachments/assets/fa666d02-18f0-462b-b176-f77982bf4b2d" />





### Sales Volume  
* Sales volumes followed a recurring yearly cycle, rising steadily from January through May, peaking in May, then dipping mid-year before recovering toward the end of the year. The last quarter of 2025 recorded stronger volumes compared to the same period in 2024.
* Metformin maintained steady demand across both years, consistent with its chronic-use nature. Ciprofloxacin showed sharp peaks in mid-2024 and early 2025, suggesting episodic demand, while Artemisinin displayed the highest volatility, likely linked to malaria incidence and supply fluctuations.
* Blake & Sons consistently recorded the highest sales volumes, significantly ahead of other pharmacies. Blair PLC remained flat with little growth, while Abbott-Munoz showed steady expansion, gradually narrowing its gap with Blair PLC by 2025. Smaller pharmacies made only marginal contributions.
* Urban pharmacies sold more per outlet, but rural outlets collectively accounted for slightly over half of total sales (50.3%), reflecting the larger number of rural outlets and highlighting their importance to overall access.
* PharmaTrust consistently led brand performance, MediPlus showed steady growth, and BioCare exhibited unstable patterns with alternating spikes and drops. These brand movements generally followed the seasonal sales cycles.
* Artemisinin emerged as the single largest contributor to sales volumes across all brands, followed by Paracetamol and Metformin as steady contributors. Coartem and Azithromycin maintained smaller but relevant market shares.
* Overall, the sales volume analysis shows a market defined by seasonality, increased demand in 2025, concentration of sales among a few pharmacies and brands, and a delicate balance between urban and rural distribution.
<img width="420" height="287" alt="image" src="https://github.com/user-attachments/assets/6f4c0ea5-2b55-4687-a51d-f40546fac812" /><img width="499" height="289" alt="image" src="https://github.com/user-attachments/assets/9bc64de5-f703-4af3-bf77-51ee0f01659a" /><img width="428" height="283" alt="image" src="https://github.com/user-attachments/assets/9bafc0c1-c7cc-4ae7-a35b-b52fe25403f7" /><img width="492" height="282" alt="image" src="https://github.com/user-attachments/assets/041306d8-0f2b-444e-84b6-8b6489be8ce8" /><img width="483" height="308" alt="image" src="https://github.com/user-attachments/assets/06f6eba0-06c9-490b-82f6-55edc78f4bec" /><img width="417" height="308" alt="image" src="https://github.com/user-attachments/assets/0fb2d5ad-795e-47b8-a306-58d940dca3d4" />
      
### Brand Diversity
* Eight distinct brands were identified alongside a few unknown ones
* The market share was balanced across four major brands (MediPlus, BioCare, PharmaTrust, HealthFirst), each holding approx. 20–22%.
* Minor brands make up 15% combined and unknown brands make up 0.1% of the total market share.
* Over time, brand diversity showed instability, as several drugs that consistently had all eight brands in circulation suddenly dropped to just 2–3 brands around May 2025. This sudden drop was also observed across multiple suppliers and pharmacies, coinciding with an overall drop in drug quantities sold.
* Location analysis showed that the pricing of mainstream brands was relatively stable across urban and rural areas, but unknown or rare brands often appeared at abnormal prices, particularly in rural markets.  
    <img width="458" height="289" alt="image" src="https://github.com/user-attachments/assets/c170a8bb-b0c2-4732-8bbf-26413e9253d9" /><img width="495" height="291" alt="image" src="https://github.com/user-attachments/assets/210597a9-b313-4c64-a4d2-8c7021b69a02" />
    <img width="949" height="353" alt="image" src="https://github.com/user-attachments/assets/7b6eb385-5725-4f78-9e81-6d77d2515129" />




### Feature Engineering
To sharpen further analysis, new features, based on the features we have, were created to capture hidden patterns  
* Brand Popularity, because counterfeit drugs often appear under rare or unknown brands and by quantifying how common each brand is in the dataset, we can identify suspicious ones.
* Price per Pharmacy, to check if the pharmacy’s prices are consistently lower than those of its peers
* Supplier Switch per Pharmacies, that checks for frequent or sudden supplier changes (especially for the same drug), because legitimate pharmacies typically have stable supplier relationships.
* Supplier Quantity Deviation, that flags any transaction done in a month where the supplier supplies a quantity of drug more than they would normally sell. Selling a huge quantity of drugs much more than you would normally sell, can be a huge red flag.
* Market Price Deviation, that flags any transaction with price, much higher than the average market price, by at least 2 standard deviations.
* Near Expiry Days, which checks the days to or days past the expiry date of a drug. This is because when drugs are near their expiry date or past, suppliers or pharmacies tend to reduce the prices and increase quantities for quick sell-out
* Undercut Market Price: which checks for prices that are at least 30% lower than the median price
* Overpriced vs Market, which checks to see if a given price is much more expensive than the normal market price.  
## Modelling
For anomaly detection, we focused on testing three models: Isolation Forest, One-Class SVM, and Self-Training SVM.  
*	**Isolation Forest & One-Class SVM**  
These models are unsupervised anomaly detection algorithms. Both require a parameter that defines the expected proportion of anomalies (contamination rate). In our case, we set this cut-off at 2% (≈200 transactions). The models then learn the distribution of the data and assign anomaly scores to each transaction.
  - A negative score indicates that the entry is considered normal.
  - A positive score indicates that the entry is anomalous.
* **Self-Training SVM**  
After running Isolation Forest, the predicted labels (normal or anomaly) were used to train a Self-Training SVM. This semi-supervised approach iteratively refines its decision boundary by combining features in different ways to learn how they contribute to anomaly classification. Importantly, it also examines unlabeled entries, estimating whether they share characteristics with anomalies, and updates its predictions accordingly.
* **Consensus Approach**  
Since each model has different sensitivities, we compared the outputs across all three. The anomalies that were consistently flagged by all three models were considered the most reliable anomalies. These consensus results now form the basis of further investigation into suspicious suppliers, pharmacies, brands, and drugs.
