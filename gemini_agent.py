import os
from google.cloud import aiplatform_v1beta1 as aip

class GeminiAgent:
    """
    A class to interact with Vertex AI Search and run search queries.
    """

    def __init__(self, project_id: str, location: str):
        self.project_id = project_id
        self.location = location
        credentials_path = "your_credentials_here"
        if os.path.exists(credentials_path):
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
        else:
            print(f"Credential path not found {credentials_path}")
        self.client_options = {"api_endpoint": aip.gapic_endpoint}
        self.client = aip.SearchServiceClient(client_options=self.client_options)

    def run_search_query(self, query: str):
        """
        Sends a search query to Vertex AI Search and returns the results.
        """
        request = aip.SearchRequest(
            query=query,
            search_engine_id="your_search_engine_id",
            
        )
        response = self.client.search(request=request)
        return response

    def get_search_results(self, response):
        """
        Gets the search results.
        """
        # Process the response here, for example, convert to JSON
        results = []
        for doc in response.matching_documents:
            results.append({"document": doc.document.content})
        return results

    def process_search_results(self, query: str):
        """
        Processes the search results.
        """
        response = self.run_search_query(query=query)
        results = self.get_search_results(response)
        from evaluation.evaluator import calculate_quality, calculate_relevance
        quality = calculate_quality(results=results)
        relevance = calculate_relevance(query=query, results=results)
        from evaluation.reporting import create_report
        report = create_report()
        report.add_metric("quality", quality)
        report.add_metric("relevance", relevance)
        report.display_report()
        return results
