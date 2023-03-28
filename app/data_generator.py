# Import required libraries
# data transformation
import pandas as pd
import random,datetime

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

        data = {'contract_key': list(contract_keys),
                'date_of_birth': date_of_births,
                'nett_salary': nett_salaries,
                'gender': genders,
                'province': provinces,
                'language': languages,
                'phone': phones}


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

        agent_codes = [random.randint(1, 8) for i in range(subset_size)]

        segments = [random.choice(['orange', 'blue', 'green', 'purple']) for i in range(subset_size)]

        subset_data = {'contract_key': subset_contract_keys,
                    'agent_code': agent_codes,
                    'segment': segments}

        sales = pd.DataFrame(subset_data)

        return sales
    
    def agent_info_table(self) -> pd.DataFrame:
        names = ['adrian', 'xolani', 'prince', 'roxanne', 'tanita', 'asanda', 'ariel', 'mikayla']
        num_agents = len(names)

        agent_codes = [i+1 for i in range(num_agents)]

        agent_names = names

        genders = ['male' if name in ['adrian', 'xolani', 'prince', 'asanda'] else 'female' for name in agent_names]

        data = {'agent_code': agent_codes,
                'agent_name': agent_names,
                'gender': genders}

        agent_info = pd.DataFrame(data)

        return agent_info