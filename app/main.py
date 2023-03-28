from data_generator import PseudoData
from mongodb_connector import MongoConnection


def main():

    # Generate data
    generate_sample = PseudoData(10000,5000)
    ci_df = generate_sample.customer_information_table()
    sales_df = generate_sample.sales_table()
    agent_df = generate_sample.agent_info_table()

    # Upload to Mongodb

    # You will need to insert the password in the string below

    cluster = MongoConnection("lliebenberg93",<PASSWORD>,"phobos.psf7kxf.mongodb.net/?retryWrites=true&w=majority")

    # Customer Information

    db = cluster["sales_demo"] # databse

    ci_df.reset_index(drop = True,inplace = True)
    collection = db["customer_information"] # table
    data_client_info = ci_df.to_dict('records')
    collection.insert_many(data_client_info)

    sales_df.reset_index(drop = True,inplace = True)
    collection = db["sales"] # table
    data_sales_info = sales_df.to_dict('records')
    collection.insert_many(data_sales_info)

    agent_df.reset_index(drop = True,inplace = True)
    collection = db["agent_info"] # table
    data_agent_info = agent_df.to_dict('records')
    collection.insert_many(data_agent_info)

if __name__=="__main__":
    main()
