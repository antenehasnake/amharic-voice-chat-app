
#### `App.js` (Frontend Code)
```javascript
import React, { useState } from "react";
import { Button, Text, View, TextInput } from "react-native";

const VoiceChatApp = () => {
  const [userInput, setUserInput] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = async () => {
    try {
      // Send user input to the backend
      const backendResponse = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: userInput }),
      });

      const data = await backendResponse.json();
      setResponse(data.response); // Adjust based on DeepSeek's response structure
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <View style={{ padding: 20 }}>
      <TextInput
        placeholder="Type your message in Amharic"
        value={userInput}
        onChangeText={setUserInput}
        style={{ borderWidth: 1, padding: 10, marginBottom: 10 }}
      />
      <Button title="Send" onPress={handleSend} />
      <Text style={{ marginTop: 20 }}>Response: {response}</Text>
    </View>
  );
};

export default VoiceChatApp;
