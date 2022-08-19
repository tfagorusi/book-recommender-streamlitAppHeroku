import pickle
import streamlit as st

def recommend(book):
    index = book_pivot.index.get_loc(str(book))
    distances, suggestions = book_model.kneighbors(book_pivot.iloc[index, :].values.reshape(1, -1))
    recommended_book_titles = []
    for i in suggestions[0,1:]:
        recommended_book_titles.append(book_pivot.index[i])

    return recommended_book_titles


page_bg_img = '''
<style>
      .stApp {
  background-image: url("https://images.theconversation.com/files/45159/original/rptgtpxd-1396254731.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=600&h=400&fit=crop&dpr=1");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown('# Book Recommendation System')
book_pivot = pickle.load(open('book_pivot.pkl','rb'))
book_model = pickle.load(open('KNN_bookModel.pkl','rb'))

book_list = book_pivot.index.values
selected_book = st.selectbox("Type or select a book from the dropdown",book_list)


if st.button('Show Recommendation'):
    recommended_book_names = recommend(selected_book)
    for i in recommended_book_names:
        st.subheader(i)
