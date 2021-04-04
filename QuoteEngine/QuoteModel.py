
class QuoteModel():
    """The class for a Quote"""
    
    def __init__(self, body: str, author: str):
        """The init method for the QuoteModel

        Args:
            body (str): the quote
            author (str): the author of the quote
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Representation of QuoteModel

        Returns:
            QuoteModel: returns QuoteModel representation
        """
        return f'QuoteModel(body={self.body}, author={self.author})'