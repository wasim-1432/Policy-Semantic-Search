import streamlit as st

from src.search import PolicySearch


st.set_page_config(
    page_title="Policy Semantic Search",
    page_icon="🔎"
)


st.title("🔎 Policy Semantic Search")

st.write(
    "Search company policies using semantic search "
    "and metadata filters."
)


@st.cache_resource
def load_search_engine():

    return PolicySearch()


search_engine = load_search_engine()


st.sidebar.header("Metadata Filters")


department = st.sidebar.selectbox(
    "Department",
    [
        "",
        "HR",
        "IT",
        "Finance"
    ]
)


document_type = st.sidebar.selectbox(
    "Document Type",
    [
        "",
        "Leave Policy",
        "Security Policy",
        "Expense Policy",
        "Remote Work Policy"
    ]
)


date = st.sidebar.text_input(
    "Date",
    placeholder="YYYY-MM-DD"
)


access_level = st.sidebar.selectbox(
    "Access Level",
    [
        "",
        "Employee",
        "Manager"
    ]
)


query = st.text_input(
    "Ask your question",
    placeholder="Example: How many annual leaves can employees take?"
)


if st.button("Search"):

    if not query:

        st.warning("Please enter a search query.")

    else:

        results = search_engine.search(
            query=query,
            department=department or None,
            document_type=document_type or None,
            date=date or None,
            access_level=access_level or None,
            k=5
        )

        st.subheader(
            f"Found {len(results)} results"
        )

        if not results:

            st.info(
                "No matching policy found."
            )

        for i, result in enumerate(results):

            st.markdown(
                f"### Result {i + 1}"
            )

            st.write(
                f"**Similarity Score:** "
                f"{result['score']:.4f}"
            )

            metadata = result["metadata"]

            st.write(
                f"**Department:** "
                f"{metadata['department']}"
            )

            st.write(
                f"**Document Type:** "
                f"{metadata['document_type']}"
            )

            st.write(
                f"**Date:** "
                f"{metadata['date']}"
            )

            st.write(
                f"**Access Level:** "
                f"{metadata['access_level']}"
            )

            st.write(
                f"**Source:** "
                f"{metadata['source']}"
            )

            st.info(
                result["text"]
            )

            st.divider()