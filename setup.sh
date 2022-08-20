mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"fagorusi_tolu08@yahoo.co.uk\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
echo $PORT
