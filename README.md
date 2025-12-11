# Mohamed Zouari - Portfolio Website

A modern, Jekyll-powered portfolio website showcasing my work as a Senior Software Engineer.

## 🚀 Features

- **Static Site Generator**: Built with Jekyll for easy maintenance
- **DRY Architecture**: Reusable components (sidebar, navigation, layouts)
- **Responsive Design**: Works on all devices
- **Modern CSS**: CSS custom properties for easy theming
- **Performance Optimized**: CDN-based fonts and icons, deferred JavaScript
- **SEO Ready**: Optimized meta tags and structure
- **GitHub Pages Ready**: Native Jekyll support

## 📁 Project Structure

```
zouariste.github.io/
├── _config.yml              # Jekyll configuration
├── _layouts/                # Page templates
│   ├── default.html         # Default layout for pages
│   └── home.html            # Homepage layout
├── _includes/               # Reusable components
│   ├── head.html            # HTML head section
│   ├── sidebar.html         # Sidebar with avatar
│   └── navigation.html      # Navigation menu
├── _data/                   # Structured data files
│   ├── navigation.yml       # Navigation links
│   └── social.yml           # Social media links
├── _sass/                   # Sass partials (if needed)
├── css/                     # Stylesheets
│   └── custom.css           # Main stylesheet
├── scripts/                 # JavaScript files
│   ├── script.js            # Main JS
│   └── disqus.js            # Disqus integration
├── images/                  # Image assets
├── index.html               # Homepage
├── summary/                 # Summary page
├── portfolio/               # Portfolio page
├── experience/              # Work experience page
├── certifications/          # Certifications page
├── references/              # References page
├── externalactivities/      # External activities page
├── contact/                 # Contact page
├── Gemfile                  # Ruby dependencies
└── README.md                # This file
```

## 🛠️ Local Development Setup

### Prerequisites

- Ruby (>= 2.7)
- RubyGems
- Bundler

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/zouariste/zouariste.github.io.git
   cd zouariste.github.io
   ```

2. **Install Ruby dependencies**
   ```bash
   gem install bundler
   bundle install
   ```

3. **Run the development server**
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site**
   Open your browser and navigate to: `http://localhost:4000`

### Development Server with Live Reload

```bash
bundle exec jekyll serve --livereload
```

This will automatically refresh your browser when you make changes.

## 📝 Making Changes

### Updating Content

1. **Edit pages**: Modify the HTML files in page folders (e.g., `summary/index.html`)
2. **Update navigation**: Edit `_data/navigation.yml`
3. **Update social links**: Edit `_data/social.yml`
4. **Site configuration**: Edit `_config.yml`

### Adding a New Page

1. Create a new folder: `mkdir newpage`
2. Create `newpage/index.html` with front matter:
   ```yaml
   ---
   layout: default
   title: New Page
   permalink: /newpage/
   ---

   <h1>Your content here</h1>
   ```
3. Add the page to navigation in `_data/navigation.yml`

### Customizing Styles

- Main styles: `css/custom.css`
- CSS variables: Edit `:root` section in `css/custom.css`
- Colors, fonts, spacing are all controlled via CSS custom properties

### Modifying Layout

- **Sidebar**: Edit `_includes/sidebar.html`
- **Navigation**: Edit `_includes/navigation.html`
- **Head section**: Edit `_includes/head.html`
- **Default layout**: Edit `_layouts/default.html`
- **Homepage layout**: Edit `_layouts/home.html`

## 🚀 Deployment

### GitHub Pages (Automatic)

1. Push your changes to the `main` branch:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

2. GitHub Pages will automatically build and deploy your site!

3. Your site will be available at: `https://yourusername.github.io`

### Manual Build

To build the site manually:

```bash
bundle exec jekyll build
```

The generated site will be in the `_site/` directory.

## 🔧 Configuration

### Site Settings

Edit `_config.yml` to update:
- Site title and description
- Author information
- Social media links
- Theme color
- Disqus integration

### Navigation Links

Edit `_data/navigation.yml` to:
- Add new navigation items
- Change link order
- Update link URLs

### Social Media Links

Edit `_data/social.yml` to:
- Add new social profiles
- Update existing links
- Change icons

## 📦 Dependencies

- **Jekyll**: Static site generator
- **kramdown**: Markdown processor
- **Google Fonts**: Roboto font family
- **Font Awesome 4.7**: Icon library

## 🎨 Customization Tips

### Changing Colors

Edit CSS custom properties in `css/custom.css`:

```css
:root {
  --color-primary: #0a66c2;    /* Main brand color */
  --color-sidebar-bg: rgba(10, 102, 194, 0.58);
  --color-tech-tag: rgba(12, 68, 124, 0.58);
}
```

### Changing Fonts

Update the Google Fonts link in `_includes/head.html` or modify:

```css
:root {
  --font-family-base: 'Roboto', Helvetica, sans-serif;
}
```

### Responsive Breakpoints

Adjust breakpoints in `css/custom.css`:

```css
:root {
  --breakpoint-xs: 450px;
  --breakpoint-sm: 568px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1001px;
}
```

## 🐛 Troubleshooting

### Jekyll doesn't start

```bash
bundle update
bundle exec jekyll serve --trace
```

### CSS changes not appearing

Clear Jekyll cache:
```bash
bundle exec jekyll clean
bundle exec jekyll serve
```

### Navigation not highlighting current page

Make sure your page's `permalink` in front matter matches the URL structure.

## 📚 Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Mohamed Zouari**
- Email: mzouari@outlook.com
- LinkedIn: [mohamed-zouari](https://www.linkedin.com/in/mohamed-zouari)
- GitHub: [zouariste](https://github.com/zouariste)
- Stack Overflow: [mohamed-zouari](https://stackoverflow.com/users/11797839/mohamed-zouari)

## 🎯 Version History

- **v2.0.0** (2025-12-11): Converted to Jekyll static site generator
- **v1.0.0**: Initial HTML/CSS/JS portfolio site

---

**Built with ❤️ using Jekyll**
