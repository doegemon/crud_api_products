import requests
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.title("Product Management")


def show_response_message(response):
    """
    Function that is used to show detailed error messages.
    """
    if response.status_code == 200:
        st.success("Operation successfully completed!")
    else:
        try:
            data = response.json()
            if "detail" in data:
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Error: {errors}")
                else:
                    st.error(f"Error: {data['detail']}")
        except ValueError:
            st.error("Unknow error. The response could not be decoded.")


# Adding Product
with st.expander("Add a New Product"):
    with st.form("new_product"):
        name = st.text_input("Product Name")
        description = st.text_area("Product Description")
        price = st.number_input("Product Price", min_value=0.01, format="%f")
        category = st.selectbox(
            "Product Category",
            ["Electronics", "Home Appliances", "Furniture", "Clothing", "Footwear"],
        )
        vendor_email = st.text_input("Vendor E-mail")
        submit_button = st.form_submit_button("Add Product")

        if submit_button:
            response = requests.post(
                "http://backend:8000/products/",
                json={
                    "name": name,
                    "description": description,
                    "price": price,
                    "categoria": category,
                    "email_fornecedor": vendor_email,
                },
                timeout=20,
            )

            show_response_message(response)

# Show All Products
with st.expander("Show All Products"):
    if st.button("Display All Products"):
        response = requests.get("http://backend:8000/products/", timeout=20)

        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame(product)

            df = df[
                [
                    "id",
                    "name",
                    "description",
                    "price",
                    "category",
                    "vendor_email",
                    "created_at",
                ]
            ]

            st.write(df.to_html(index=False), unsafe_allow_html=True)

        else:
            show_response_message(response=response)

# Show a Specific Product
with st.expander("Get Product Details"):
    get_product_id = st.number_input("Product ID", min_value=1, format="%d")

    if st.button("Product Search"):
        response = requests.get(
            f"http://backend:8000/products/{get_product_id}", timeout=20
        )

        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame([product])

            df = df[
                [
                    "id",
                    "name",
                    "description",
                    "price",
                    "category",
                    "vendor_email",
                    "created_at",
                ]
            ]

            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Delete Product
with st.expander("Delete Product"):
    delete_product_id = st.number_input(
        "Product ID to Delete", min_value=1, format="%d"
    )
    if st.button("Delete Product"):
        response = requests.delete(
            f"http://backend:8000/products/{delete_product_id}", timeout=20
        )
        show_response_message(response)

# Update Product
with st.expander("Update Product"):
    with st.form("update_product"):
        update_product_id = st.number_input("Product ID", min_value=1, format="%d")
        new_name = st.text_input("New Product Name")
        new_description = st.text_area("New Product Description")
        new_price = st.number_input("New Product Price", min_value=0.01, format="%f")
        new_category = st.selectbox(
            "New Product Category",
            ["Electronics", "Home Appliances", "Furniture", "Clothing", "Footwear"],
        )
        new_vendor_email = st.text_input("New Vendor E-mail")
        update_button = st.form_submit_button("Update Product")

        if update_button:
            update_data = {}

            if new_name:
                update_data["name"] = new_name
            if new_description:
                update_data["description"] = new_description
            if new_price > 0:
                update_data["price"] = new_price
            if new_category:
                update_data["category"] = new_category
            if new_vendor_email:
                update_data["vendor_email"] = new_vendor_email

            if update_data:
                response = requests.put(
                    f"http://backend:8000/products/{update_product_id}",
                    json=update_data,
                    timeout=20,
                )
                show_response_message(response)
            else:
                st.error("No product information provided for update.")
