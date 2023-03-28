import pandas as pd
import random,datetime
import numpy as np

class PseudoData:
    def __init__(self, applications :int, activations :int):
        self.applications = applications
        self.activations = activations

    def customer_information_table(self) -> pd.DataFrame:
        num_entries = self.applications
        contract_keys = set()
        while len(contract_keys) < num_entries:
            contract_keys.add(random.randint(10000, 99999))

        today = datetime.date.today()
        date_of_births = [today - datetime.timedelta(days=random.randint(18, 60)*365) for i in range(num_entries)]

        nett_salaries = [random.randint(3500, 20000) for i in range(num_entries)]

        genders = [random.choice(['male', 'female']) for i in range(num_entries)]

        provinces = [random.choice(['GP', 'WC', 'EC', 'NC', 'FS', 'LP', 'MP', 'NW', 'KZN']) for i in range(num_entries)]

        languages = [random.choice(['English', 'Afrikaans', 'Xhosa', 'Zulu', 'Sesotho']) for i in range(num_entries)]

        phones = [random.choice(['082', '076', '086', '081', '061', '084']) + ''.join(random.choices('0123456789', k=7)) for i in range(num_entries)]

        agent_codes = []
        for i in range(num_entries):
            if date_of_births[i].year < 1980 and nett_salaries[i] < 5000 and genders[i] == 'male' and provinces[i] in ['EC', 'NC', 'WC'] and languages[i] in ['Xhosa', 'English']:
                agent_codes.append(1)
            elif date_of_births[i].year > 1990 and nett_salaries[i] < 10000 and genders[i] == 'male' and provinces[i] in ['KZN', 'GP'] and languages[i] in ['Zulu', 'English']:
                agent_codes.append(2)
            elif date_of_births[i].year > 1980 and nett_salaries[i] > 10000 and genders[i] == 'female' and provinces[i] in ['GP', 'WC', 'MP', 'LP'] and languages[i] == 'English':
                agent_codes.append(3)
            elif date_of_births[i].year > 1995 and nett_salaries[i] < 10000 and languages[i] in ['Sesotho', 'English'] and provinces[i] in ['FS', 'MP', 'LP', 'NW']:
                agent_codes.append(4)
            elif date_of_births[i].year < 1970 and nett_salaries[i] < 10000 and genders[i] == 'female' and languages[i] in ['English', 'Afrikaans'] and provinces[i] in ['WC', 'NC']:
                agent_codes.append(5)
            else:
                agent_codes.append(random.randint(1, 5))

        data = {'contract_key': list(contract_keys),
                'date_of_birth': date_of_births,
                'nett_salary': nett_salaries,
                'gender': genders,
                'province': provinces,
                'language': languages,
                'phone': phones,
                'agent_code': agent_codes}

        ci = pd.DataFrame(data)

        ci.date_of_birth = ci.date_of_birth.astype("string") # since mongob db cannot interpret pandas datetime objects

        self.ci = ci

        return ci
    

    def sales_table(self) -> pd.DataFrame:
        # create the sales dataframe

        subset_size = self.activations
        num_entries = self.applications

        subset_indices = random.sample(range(num_entries), subset_size)

        subset_contract_keys = [self.ci.loc[i, 'contract_key'] for i in subset_indices]

        segments = np.random.choice(['orange', 'blue', 'green', 'purple'], size=subset_size, p=[0.6, 0.2, 0.15, 0.05])

        subset_data = {'contract_key': subset_contract_keys,
                    'segment': segments}

        sales = pd.DataFrame(subset_data)

        return sales
    
    def agent_info_table(self) -> pd.DataFrame:

        data = {'agent_code': [1, 2, 3, 4, 5],
        'agent_name': ['Xolani', 'Asanda', 'Ariel', 'Prince', 'Tanita']}

        agents = pd.DataFrame(data)

        return agents

# x =PseudoData(10000,5000)

# df1 = x.customer_information_table()

# df2 = x.sales_table()

# print(df1.head())
# print(df2.head())