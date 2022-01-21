# PIRD_Decision_Making
This Github regroup all files related to the PIRD of Florian Merindol and Asmae Kharrab. The subject is the sensitivity analysis and the Simos-Roy-Figueira weighting of the Electre Tri method

# ELECTRE-Tri MCDA Python

Authors: [Florian MERINDOL](mailto:florian.merindol@insa-lyon.fr)
 [Asmae KHARRAB](mailto:asmae.kharrab@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), France, 21/01/2022

[**Sensitivity_analysis.py**](ELECTRE_Tri.py) is a method of sensitivity analysis on the Electre Tri method. A Jupiter Notebook explains how the code works. 

[**Calculate_SRF.py**](ELECTRE_Tri.py) is a method of weighting based on the Simos Roy Figueira method. A Jupiter Notebook explains how the code works. 


## 2. Quick explanations
In order to realize the weighting :
- Execute the "Calculate_SRF" file

In order to make the sensitivity analysis : 
- Run the "Sensitivity_analysis" file

You shouldn't have to run all other files to run successfully the previous codes. 

## 3. Contents
### 3.1 Tutorials

[Tutorial_Calculate_SRF.ipynb](Tutorial_Calculate_SRF.ipynb): Tutorial explaining how the calculation code [Calculate_SRF.py](Calculate_SRF.py) is built.

[Tutorial_Sensivitity_analysis.ipynb](Tutorial_Sensivitity_analysis.ipynb): Tutorial explaining how the calculation code [Sensivitity_analysis.py](Sensivitity_analysis.py) is built.

### 3.2 Examples
#### 3.2.1 Description

[Description_Building_retrofit_scenarios.md](Description_Building_retrofit_scenarios.md): Document describing the origin and composition of the data for the example of multi-criteria decision support for the retrofit scenarios of a collective housing building.

[Description_Wall_insulation_scenarios.md](Description_Wall_insulation_scenarios.md): Document describing the origin and composition of the data related to the example of multi-criteria decision support for external thermal insulation scenarios of a collective housing building.

*Note: The description documents are used to explain how the examples are constructed and what they are made of.* 

#### 3.2.2 XLS files

[Performances - insulation scenarios.xls](Performances - insulation scenarios.xls): XLS file containing the performances of insulation scenarios.

[Performances - renovation scenarios.xls](Performances - renovation scenarios.xls): XLS file containing the performances of renovation scenarios.

[Weighting - renovation scenarios.xlsx](Weighting - renovation scenarios.xlsx): XLSX file containing the weighting of renovation scenarios.

#### 5.2. PY files

[Calculate_SRF.py](Calculate_SRF.py): PY file containing the Simos Roy Figueira method.

[ELECTRE_TRI_B.py](ELECTRE_TRI_B.py): PY file containing the Electre Tri B function.

[ELECTRE_TRI_B_main_test.py](ELECTRE_TRI_B_main_test.py): PY file containing the Electre Tri B implementation method.

[Sensitivity_analysis.py](Sensitivity_analysis.py): PY file containing the sensitivity analysis.

[Python_interpreter]:https://www.python.org/



