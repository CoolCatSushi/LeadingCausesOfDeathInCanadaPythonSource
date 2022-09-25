    # Leading Causes of Death in Canada
    #### Video Demo:  https://youtu.be/PvKzjOpzHMU
    #### Description:
    #### A Python program with Tkinter GUI to filter and display statistical data from CSV files. Currently fitted to display leading causes of death in Canada provided via Canada Open Data.
            Can be easily tweaked to accomodate other CSV datasets with similar features and customized to suit user needs.

    #### Features:
            Expand filter windows for ease of selection, and minimize to accomodate varying window sizes.
            Cute interface with contrasting colors to view data clearly.
            Ability to select rows of interest within tables for clear viewing.
            Ability to add additional tables to workspace by re-selecting filters, allowing for multiple selection combinations.
            Multi-selection for causes, ages and years. Program is built to give accurate data for each combination of filters, if chosen.
                Sex field does not allow for multi-selection since it wouldn't be a highly useful feature and would increase the load time of the program.
            Tables organized under year --> age --> causes.
                Compare data for each cause of death, per age group, per year. Intuitive organization.
                Ages are grouped under years, and each data type is labelled per year in an intuitive way.
            Cause of death and Year are mandatory fields and display error messages if not selected.
                Cause of death is prioritized and therefore if neither field is selected, then error message for Cause will display.
            Age group defaults to 'All ages' if not selected.
                Since this dataset focuses on Cause of Death, it doesn't make sense to apply a default value for this field.
                Years are more arbitrary than age, since there is a true limit to number of age groups (within human lifespan), however years included here are constrained by the data
                Therefore, it would not be user friendly to apply a default value for the Years field.

    #### Future Developments:
            The hope for this project is to expand it to be easily applicable for reading any healthcare related dataset with similar features, as well as allow it to be compatible with Live data.
            I would also like to incorporate more advanced statistical analysis and graphical forms to view the data.
            Finally, I'd like to transfer the project to a newer GUI with more capabilities.

    #### Files:
            project.py: Project file, including all functions required to run the program.
            README.md: Project description.
            requirements.txt: PIP installed imports required to run the program.
            13100394_MetaData.csv: MetaData file including information to organize the dataset
            13100394.csv: Dataset file from Statistics Canada, including Mortality data across Canada from 2000-2020.
            test_project.py: File including all test functions to ensure proper functioning of the program.

    #### Required Files:
            Open data leading causes of death in canada CSV files from Statistics Canada. Includes CSV MetaData and CSV Data files in Data folder.

    #### Program Execution:
            In program root folder, run: 'python ./project.py'