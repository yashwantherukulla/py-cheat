# FastAPI Clipboard Assistant

This is a FastAPI application that interacts with the clipboard, processes the content using a language model, and returns the processed content. The application uses HTML templating to render forms and display results.

## Features

- **Form Handling**: Submit data through a form and copy it to the clipboard.
- **Clipboard Content Processing**: Fetch content from the clipboard, process it using a language model, and display the result.
- **HTML Templating**: Render HTML templates for form submission and displaying results.


## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/shreeyash-ugale/py-cheat
    cd py-cheat
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your `GROQ_API_KEY`:
    ```
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. **Run the application**:
    ```sh
    uvicorn main:app --reload
    ```

2. **Access the application**:
    Open your browser and go to `http://127.0.0.1:3100`.

## Endpoints

- **GET /**: Returns a simple "Hello, World!" message.
- **GET /send**: Renders the form for data submission.
- **POST /form**: Handles form submission and copies the data to the clipboard.
- **GET /clip**: Fetches content from the clipboard, processes it, and displays the result.

## HTML Templates

- **form.html**: Template for the form submission page.
- **disp.html**: Template for displaying the processed clipboard content.

## Example

1. **Submit Data**:
    - Go to `http://127.0.0.1:3100/send`.
    - Enter data in the form and submit.

2. **View Processed Clipboard Content**:
    - Go to `http://127.0.0.1:3100/clip` to view the processed content.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Jinja2](https://palletsprojects.com/p/jinja/)
- [pyperclip](https://github.com/asweigart/pyperclip)
- [Groq](https://groq.com/)
- [Instructor](https://instructor.com/)



#### Use at your own risk