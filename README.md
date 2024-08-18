### README

#### Overview
This script interacts with the Reddit API to fetch posts and comments from specified subreddits based on keywords. It authenticates using Reddit's OAuth2 API, searches for posts matching given keywords, retrieves comments for these posts, and finally writes the data to a CSV file.

#### Requirements
- Python 3.x
- Libraries: `requests`, `csv`

You can install the required libraries using:
```bash
pip install requests
```

#### How to Run
1. **Save the Script**: Save the Python script as `reddit_scraper.py`.

2. **Update Authentication Details**:
   - Replace `'user_name'` with your Reddit username.
   - Replace `'pswd'` with your Reddit password.
   - Replace `'user_id'` with your Reddit application client ID.
   - Replace `'access_token'` with your Reddit application secret.

3. **Execute the Script**: Open your terminal or command prompt and run the script using:
   ```bash
   python reddit_scraper.py
   ```

4. **View Output**: The script will generate a file named `reddit_data.csv` containing the scraped data.

#### Script Functions
- **`authenticate()`**: Authenticates with the Reddit API and retrieves an access token.
- **`fetch_comments(post_id, token)`**: Fetches comments for a given post ID using the access token.
- **`fetch_data(token, subreddits, keywords)`**: Searches posts in specified subreddits using given keywords, retrieves comments, and aggregates data.
- **`write_to_csv(data, filename='reddit_data.csv')`**: Writes the aggregated data to a CSV file.

#### Assumptions
- The script assumes that the Reddit API credentials and application settings are correct.
- Reddit API endpoints and response formats are assumed to be as expected.

#### Limitations
- **Authentication**: Ensure that you have valid Reddit API credentials. The script will fail if authentication details are incorrect.
- **API Rate Limits**: Reddit's API has rate limits which may affect data retrieval if the script is run frequently or with large query parameters.
- **Data Formatting**: Comments are joined by ' | ' and might not retain complex formatting.

#### Notes
- Ensure that your Reddit app has the necessary permissions for accessing posts and comments.
- The `fetch_comments` function needs to be completed to return a list of comments; currently, it only initializes the `comments_list`.

Make sure to review Reddit's API documentation for more details on API usage and authentication: [Reddit API Documentation](https://www.reddit.com/dev/api/).
