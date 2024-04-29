# Analysis of Immunosenescence on Epidemic and Vaccine Modeling 
  Varying factors can contribute to susceptibility to disease among populations. One particular factor to consider is age and the development of immunosenescence. Immunosenescence is the alteration of immune function, typically thymic involution causing the decreased functions of T and B cells, due to aging (Rink & Wessels, 2022). Both of these cell types are involved in the acquisition or antigen-specific immune response such that they are the only cells in an organism that can recognize and respond to that specific antigen epitope (Cano & Lopera, 2013). In immunosenescence the number of memory T and B cells increase, while the response to new antigens decreases. Similarly, this decreases the function of granulocytes, macrophages, and NK cells (Rink & Wessels, 2022). 
  The importance of immunosenescence and aging was especially emphasized during the COVID-19 pandemic in 2020. Increased susceptibility to disease due to immunosenescence could play a huge role in the way mathematical and computational methods model disease and immunity as provided by vaccinations. This project seeks to explore how immunosenescence can be mathematically modeled using an SEIRS model, and how this idea can be applied to vaccination models. 
# Method
To analyze varying susceptibility among different age groups, we developed an SEIRS model and modified it to include a variable termed 'T'. This variable represents the varying loss of immunity due to immunosenescence. This modification allowed us to formulate a set of ordinary differential equations (ODEs) with 'T' varying based on age. Additionally, we created a contact matrix for the different age groups, considering a total population size of 145 individuals (including 55 parents, 30 children, and 60 grandparents). Subsequently, we wrote code to calculate the varying $R_0$ values and saved the results to a CSV file named 'simulation_results.csv'. We then manipulated this data using a Leaky Vaccination Model with varying Vaccine Efficacy (VE), examining scenarios where VE was 0, 1, and 0.8. Finally, we visualized each age group's data using bar charts generated with the Matplotlib library in Python.

# SEIRS Model:
![D1A78702-E204-4E51-94CB-1595EF1F787F_1_201_a](https://github.com/saba2735/Infectious_Disease_Project/assets/123501165/d1beff20-20c5-4295-850d-7b77bd118a1b)

# Modified SEIRS Model to Include T Based on Age Group:
  ![7A252579-3948-4CFB-B9EA-09B956![D1A78702-E204-4E51-94CB-1595EF1F787F_1_201_a](https://github.com/saba2735/Infectious_Disease_Project/assets/123501165/4be54916-18b5-40c6-865e-ac25cf56fb13)
91437A_1_201_a](https://github.com/saba2735/Infectious_Disease_Project/assets/123501165/8e0b6573-917c-40ba-a5ed-068afa707663)

# Equations:
## SEIRS: 

<img width="235" alt="Screenshot 2024-04-29 at 10 58 44 AM" src="https://github.com/saba2735/Infectious_Disease_Project/assets/123501165/5fbcc0a4-01dc-4f8c-9460-df74c2b6e124">

## Modified SEIRS:

<img width="246" alt="Screenshot 2024-04-29 at 10 58 56 AM" src="https://github.com/saba2735/Infectious_Disease_Project/assets/123501165/414669c8-31e7-4f87-910e-e1a3d5b3dbde">

# Contact Matrix

  Assumptions: 
  Kids come into contact with 20 kids a day 
  Kids come into contact with 2 parents a day 
  Kids come into contact with 2 grandparents a day 
  Parents come into contact with 2 kids a day 
  Parents come into contact with 1 other parent a day 
  Parent come into contact with 2 grandparents a day
  Grandparents come into contact with 2 kids a day 
  Grandparents come into contact with 2 parents a day 
  Grandparents come into contact with 1 other grandparent a day 


# References
Bjørnstad, O.N., Shea, K., Krzywinski, M. et al. The SEIRS model for infectious disease dynamics. Nat Methods 17, 557–558 (2020). https://doi.org/10.1038/s41592-020-0856-2

Chapter 5Introduction to T and B lymphocytes ← book need formal citation!

Liu, Z., Liang, Q., Ren, Y. et al. Immunosenescence: molecular mechanisms and diseases. Sig Transduct Target Ther 8, 200 (2023). https://doi.org/10.1038/s41392-023-01451-2

Rink, L., & Wessels, I. (2022). Immunosenescence. In N. Rezaei (Ed.), Encyclopedia of Infection and Immunity (pp. 259-276). Elsevier. ISBN 9780323903035. https://doi.org/10.1016/B978-0-12-818731-9.00072-0. 

Mittelbrunn, M., Kroemer, G. Hallmarks of T cell aging. Nat Immunol 22, 687–698 (2021). https://doi.org/10.1038/s41590-021-00927-z

Yousefzadeh, M.J., Flores, R.R., Zhu, Y. et al. An aged immune system drives senescence and ageing of solid organs. Nature 594, 100–105 (2021). https://doi.org/10.1038/s41586-021-03547-7
