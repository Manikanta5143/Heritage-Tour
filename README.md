# Heritage Site Virtual Tour

An immersive virtual tour application that showcases historical sites with interactive features, audio narration, and a dynamic gallery.

## Features

- **Interactive Virtual Tour**
  - Smooth slide transitions between locations
  - Audio narration for each location
  - Interactive hotspots for navigation
  - Progress tracking
  - Audio controls

- **Historical Gallery**
  - Dynamic image loading
  - Category-based filtering
  - Image details modal
  - Responsive grid layout

- **Modern UI/UX**
  - Historical color scheme inspired by ancient Indian temples
  - Elegant typography with Playfair Display and Cinzel fonts
  - Responsive design for all devices
  - Smooth animations and transitions

## Tech Stack

- **Backend**
  - Python 3.x
  - Flask
  - AWS Services (for image and audio generation)
  - dotenv for environment variables

- **Frontend**
  - HTML5
  - CSS3 with custom animations
  - JavaScript (ES6+)
  - Bootstrap 5
  - Font Awesome icons
  - Google Fonts

## Prerequisites

- Python 3.x
- pip (Python package manager)
- AWS Account (for image and audio generation)
- Modern web browser

## Installation

1.Add the audio files into folder named "audio"

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your AWS credentials:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region
```

5. Create required directories:
```bash
mkdir -p static/images/gallery
mkdir -p static/images/tour
mkdir -p static/audio
```

## Project Structure

```
heritage-site-tour/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── static/
│   ├── css/
│   │   ├── style.css     # Main styles
│   │   └── tour.css      # Tour-specific styles
│   ├── js/
│   │   ├── gallery.js    # Gallery functionality
│   │   └── tour.js       # Tour functionality
│   ├── images/
│   │   ├── gallery/      # Gallery images
│   │   └── tour/         # Tour images
│   └── audio/            # Audio narration files
├── templates/
│   ├── index.html        # Home page
│   ├── gallery.html      # Gallery page
│   └── tour.html         # Tour page
└── utils/
    ├── image_generator.py # Image generation utility
    └── audio_generator.py # Audio generation utility
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

### Virtual Tour
- Use the navigation arrows to move between locations
- Click on hotspots to jump to specific locations
- Toggle audio narration using the audio button
- View location information in the info panel

### Gallery
- Browse through historical images
- Click on images to view details
- Filter images by category
- View image descriptions and historical context

## API Endpoints

- `GET /` - Home page
- `GET /gallery` - Gallery page
- `GET /tour` - Virtual tour page
- `POST /generate-image` - Generate new images
- `POST /generate-audio` - Generate audio narration

## Contributing

1. Fork the repository
2. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```
3. Commit your changes:
```bash
git commit -m 'Add some feature'
```
4. Push to the branch:
```bash
git push origin feature/your-feature-name
```
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Historical color scheme inspired by ancient Indian temples
- Fonts provided by Google Fonts
- Icons by Font Awesome
- Bootstrap framework for responsive design

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Future Enhancements

- [ ] Add more interactive elements to the tour
- [ ] Implement 360° panoramic views
- [ ] Add user authentication
- [ ] Create an admin panel for content management
- [ ] Add more historical locations
- [ ] Implement social sharing features 
