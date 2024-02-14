# Movie Information Retrieval using IMDb API and BeautifulSoup library

## 1. Which package/library does the sample program demonstrate?
   - The sample program demonstrates the usage of the BeautifulSoup library for web scraping IMDb search results.

## 2. How does someone run your program?
   - Clone the repository and install the required libraries using `pip install beautifulsoup4` and `pip install IMDbPY`.
   - Run the script using `python IMDBScraper.py`.
   - Enter the movie title.

## 3. What purpose does your program serve?
   - The program retrieves and displays information about a movie, including its title, year, IMDb rating, genres, plot summary, and cast.

## 4. What would be some sample input/output?
   - **Input:** Enter the movie title.
   - **Output:**
     ```
     Title: The Shawshank Redemption
     Year: 1994
     IMDB Rating: 9.3
     Genres: Drama
     Plot Summary: Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.
     
     Cast:
     - Tim Robbins
     - Morgan Freeman
     - ...
     ```

## References
   - [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
   - [IMDbPY Documentation](https://imdbpy.readthedocs.io/en/latest/)
