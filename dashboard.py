import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("all_datas_1.csv")

the_orders = all_df[['order_status', 'order_purchase_timestamp', 'order_id', 'customer_id', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']]
order_items = all_df[['order_id', 'order_item_id', 'product_id', 'seller_id', 'shipping_limit_date', 'price', 'freight_value']]
products = all_df[['product_id', 'product_category_name', 'product_category_name_english']]
order_items.drop_duplicates(inplace=True, keep='last')
products.drop_duplicates(inplace=True, keep='last')
the_orders.drop_duplicates(inplace=True, keep='last')

merged_products = order_items.merge(products, on='product_id')
category_counts= merged_products.groupby('product_category_name_english')['order_item_id'].count().sort_values(ascending=False)

most_5 = category_counts.head(5)
least_5 = category_counts.tail(5)

print(most_5)
print(least_5)

delivered_orders = the_orders[the_orders['order_status'] == 'delivered']
delivered_orders = delivered_orders['order_purchase_timestamp']
yearly_orders = delivered_orders.value_counts().sort_index() 

print(yearly_orders)

st.header('Olist E-Commerce Dashboard ✨📈')
st.text("     ")


st.subheader('Sales Total Per Year 💵')
#st.bar_chart(yearly_orders, color='#9283b9')
plt.figure(figsize=(12, 7))
plt.style.use('dark_background')
sns.barplot(x=yearly_orders.index, y=yearly_orders.values, palette='winter')
plt.xlabel('Tahun')
plt.ylabel('Total Sales')
st.pyplot(plt)
st.text_area("Explanations 💡", "Penjualan dari tahun 2017-2018 meningkat, dari 42.000-an ke 52.000-an penjualan di tahun 2018, atau meningkat 21% dari tahun sebelumnya. "
             "Di tahun berikutnya, kemungkinan besar penjualan akan semakin meningkat.")
st.markdown('######')
st.markdown('######')
st.markdown('######')

st.subheader('5 Most Purchased Categories 📱')
plt.figure(figsize=(12, 7))
plt.style.use('dark_background')
sns.barplot(x=most_5.index, y=most_5.values, palette='winter')
plt.xlabel('Kategori Barang')
plt.ylabel('Total Sales')
st.pyplot(plt)
st.text_area("Explanations 💡", "Kategori produk yang paling laris adalah produk yang sering dipakai sehari-hari atau kebutuhan primer. Contohnya perlengkapan mandi, perlengkapan kesehatan dan kecantikan, perlengkapan olahraga, dll. "
             "Penjualan kelima kategori produk ini tembus sampai ribuan sales.")
st.markdown('######')
st.markdown('######')
st.markdown('######')

st.subheader('5 Least Purchased Categories 📉🛒')
plt.figure(figsize=(12, 7))
plt.style.use('dark_background')
sns.barplot(x=least_5.index, y=least_5.values, palette='winter')
plt.xlabel('Kategori Barang')
plt.ylabel('Total Sales')
st.pyplot(plt)
st.text_area("Explanations 💡", "Produk yang jarang dibeli cenderung mengarah ke barang-barang sekunder. Contohnya kerajinan seni, fashion, dan lain sebagainya. Berbanding terbalik dengan kategori produk terlaris, penjualan kelima produk ini hanya mencapai puluhan sales saja.")
st.markdown('######')
st.markdown('######')
st.markdown('######')

st.header('Recommendation 📋🔎')
st.text_area("Inilah beberapa rekomendasi dari data yang telah tersaji:", "📦 Perbanyak stok kategori barang yang laris, kurangi stok barang yang tidak terlalu laris                        "
             "🏷️ Berlakukan promo untuk barang-barang yang tidak terlalu laris untuk meningkatkan jumlah sales")