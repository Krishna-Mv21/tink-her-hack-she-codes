<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# Smart Ambulance Navigation System 🎯

## Basic Details

### Team Name: She Codes

### Team Members
- Member 1: [Krishnapriya MV] - [College of Engineering Attingal]
- Member 2: [Gayathri Sunil] - [College of Engineering Attingal]

### Hosted Project Link
[https://tink-her-hack-she-codes.onrender.com/]

### Project Description
[A real time map for ambulance with advanced features designed to reduce ambulance response time and patient reach hospital faster during critical situations such as accidents or medical emergencies]
### The Problem statement
[Ambulance response time is a critical factor in determining patient outcomes during medical emergencies. Delays in ambulance arrival can lead to increased morbidity and mortality. Additionally, traffic congestion and inefficient routing can further exacerbate these delays. ]

### The Solution
[Our solution is a real-time ambulance tracking system that utilizes advanced features to reduce ambulance response time and improve patient outcomes. The system provides real-time ambulance tracking, traffic-aware routing, and efficient ambulance dispatch to ensure timely medical assistance during critical situations.]

---

## Technical Details

## Directory Structure

```text
.
├── docs/               # Documentation assets and diagrams
├── static/             # Frontend assets (CSS, JS, Images)
├── templates/          # HTML templates
├── .env                # Environment variables
├── .gitignore          # Git ignore rules
├── app.py              # Main Flask application
├── Procfile            # Deployment configuration
├── README.md           # Project documentation
└── requirements.txt     # Python dependencies
```

### Technologies/Components Used

**For Software:**
- Languages used: [e.g., JavaScript, Python, HTML, CSS]
- Frameworks used: [e.g., Flask]
- Libraries used: [e.g., Leaflet.js, Chart.js]
- Tools used: [e.g., VS Code, Git, GitHub,antigravity]

**For Hardware:**
- Main components: [List main components]
- Specifications: [Technical specifications]
- Tools required: [List tools needed]

---

## Features

List the key features of your project:
- Feature 1: [Real time ambulance tracking]
- Feature 2: [Traffic-aware routing]
- Feature 3: [Efficient ambulance dispatch]
- Feature 4: [Real time traffic updates]
- Feature 5: [Real time ambulance tracking]
]

---

  ## Implementation

  ### For Software:

  #### Installation
  ```bash
  pip install -r requirements.txt
  ```

  #### Run
  ```bash
  python app.py
  ```

  ### For Hardware:

  #### Components Required
  - **ESP32 DevKit V1**: Core microcontroller for processing and connectivity.
  - **NEO-6M GPS Module**: For acquiring real-time location coordinates.
  - **SIM800L GSM Module**: For transmitting SOS data and emergency alerts.
  - **Buzzer & LEDs**: For local emergency status indications.
  - **OLED Display (0.96")**: To show system status and GPS lock information.
  - **Push Button**: For triggering the physical S.O.S beacon.
- **Power Supply**: 5V/2A adapter or Li-ion battery with buck converter.

#### Circuit Setup
1. **GPS Connection**: Connect NEO-6M VCC to 3.3V, GND to GND, TX to ESP32 Pin 16 (RX2), and RX to Pin 17 (TX2).
2. **GSM Connection**: Connect SIM800L VCC to stable 4V/2A supply, GND to GND, TX to ESP32 Pin 27, and RX to Pin 26.
3. **SOS Button**: Connect one side of the push button to Pin 4 and the other to GND (using internal pull-up).
4. **Indicators**: Connect Buzzer to Pin 18 and Status LED to Pin 19 through a 220Ω resistor.
5. **Display**: Connect OLED SDA to Pin 21 and SCL to Pin 22.

---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![![alt text](image.png)](Screenshot of Home page)
*Add caption explaining what this shows*

![![alt text](image-1.png)](Screenshot of User Portal)
*Add caption explaining what this shows*

![![alt text](image-2.png)](Screenshot of Driver Portal)
*Add caption explaining what this shows*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*Explain your system architecture - components, data flow, tech stack interaction*

**Application Workflow:**

![Workflow](docs/workflow.png)
*Add caption explaining your workflow*

---

### For Hardware:

#### Schematic & Circuit

![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
https://drive.google.com/file/d/1oEVGUJsTp3hp2a0dDOOT_YPo-qX_miCV/view?usp=sharing

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
