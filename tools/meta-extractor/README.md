# Meta Extractor

A client-side web application for analyzing your Facebook and Instagram connections. No server required - all processing happens in your browser.

## Features

### Facebook
- **Blocked Users Viewer**: Visualize your Facebook blocked users list with profile pictures

### Instagram
- **Followers Analyzer**: See who follows you with profile pictures
- **Following Analyzer**: See who you follow
- **Unfollowers Detector**: Find people you follow who don't follow you back

## How to Use

### Live Demo

Visit the tool at: `https://[your-username].github.io/tools/meta-extractor/`

### Facebook Blocked Users

1. **Download Your Facebook Data**
   - Go to Facebook Settings → Privacy → Download Your Information
   - Select "Blocked Users"
   - Download as HTML format

2. **Use the Tool**
   - Open the "Blocked Users (Facebook)" tab
   - Copy the entire content of your blocks HTML file
   - Paste into the textarea
   - Click "Extract Data"
   - View your blocked users with profile pictures in a grid

### Instagram Followers & Following

1. **Download Your Instagram Data**
   - Go to Instagram Settings → Security → Download Data
   - Wait for the email with your data
   - Download and extract the ZIP file

2. **Extract Followers**
   - Find and open the `followers_1.html` file (or similar)
   - Copy all content
   - Paste into the "Followers (Instagram)" tab
   - Click "Extract Data"

3. **Extract Following**
   - Find and open the `following.html` file (or similar)
   - Copy all content
   - Paste into the "Following (Instagram)" tab
   - Click "Extract Data"

### Finding Unfollowers (Instagram)

1. Switch to the "Find Unfollowers (Instagram)" tab
2. Paste your "Following" HTML in the left textarea
3. Paste your "Followers" HTML in the right textarea
4. Click "Find Unfollowers"
5. See a list of people you follow who don't follow you back

## Key Features

### Smart Parsing
- **Facebook**: Extracts names and profile pictures from blocked users HTML
- **Instagram**: Parses usernames from image alt attributes (`username's profile picture`)
- **Photo Extraction**: Automatically finds images from `xlink:href` or `src` attributes
- **Fallback Avatars**: Generates letter avatars if profile pictures aren't available

### Privacy First
- **100% Client-Side**: All data processing happens in your browser
- **No Data Sent**: Nothing is uploaded to any server
- **No Storage**: Data is only kept in memory while you use the tool
- **Open Source**: All code is visible and auditable

### Platform-Specific UI
- Color-coded badges (Facebook blue, Instagram gradient)
- Platform-specific instructions
- Optimized parsers for each platform's HTML format

## Technical Details

- Pure HTML, CSS, and JavaScript
- No dependencies or frameworks
- Works on GitHub Pages
- Mobile responsive
- Handles multiple HTML formats from Meta platforms

## Browser Compatibility

Works on all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

## Tips

### For Best Results:
- Copy the **entire** HTML file content (Ctrl+A/Cmd+A in your editor)
- If extraction shows no results, try opening the HTML file in a browser, then copy from there
- The tool automatically handles duplicates
- Profile pictures are downloaded from Facebook/Instagram CDNs
- If images don't load, letter avatars are shown instead

### Troubleshooting:
- **No profiles found**: Make sure you're copying the correct HTML file
- **Photos not showing**: Check your internet connection (images load from Meta CDNs)
- **Wrong count**: Instagram data may have duplicates in the source file, tool automatically deduplicates

## Legacy Python Scripts

The old Python scripts have been removed and replaced by this web-based solution:
- ~~script_block_list.py~~ → Now: Facebook Blocked Users tab
- ~~script_followers_extractor.py~~ → Now: Instagram tabs
- ~~to_unfollow.py~~ → Now: Find Unfollowers tab

## Contributing

Feel free to submit issues or pull requests to improve the tool!

## License

MIT License - Feel free to use and modify as needed.
