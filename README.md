# Whisper Transcription Function 

This is a Python Azure Function that transcribes audio files using the [Whisper speech recognition library](https://github.com/assemblyai/whisper). 

## Getting Started

1. Clone this repository locally.
2. Install the [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash) if you haven't already.
3. Install the [Whisper library](https://github.com/assemblyai/whisper) by running `pip install whisper`.
4. Open a terminal and navigate to the cloned repository.
5. Run `func start` to start the function locally.

## Usage

You can make a GET or POST request to the function URL with the following parameters:

- `file` (required): The URL of the audio file to transcribe.
- `test_func`: A test parameter that can be set to any value to check that the function is running.

The function will return a plain text transcription of the audio file.

### Example Request

```
GET https://your-function-url.azurewebsites.net/api/transcribe?file=https://your-audio-file-url.mp3
```

### Example Response

```
This is the transcription text.
```

## Deployment

To deploy the function to Azure, follow these steps:

1. Create an Azure Function App in the Azure Portal.
2. Open the function app and navigate to **Functions** > **Add**.
3. Select **Python** as the language and **HTTP trigger** as the template.
4. Enter a name for the function and click **Create**.
5. In the function settings, set the **Runtime stack** to **Python** and the **Function app settings** > **Python version** to **3.8**.
6. In the **Platform features** tab, select **Deployment Center** and choose a deployment method.
7. Follow the instructions for your chosen deployment method.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
