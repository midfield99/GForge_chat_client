# GForge_chat_client

GForge chat client is a powerful chat bot framework built upon GForge NEXT platform. It integrates various components in GForge REST API to allow users to control the project management directly from the chat box.

Our chat client is unique in providing users with control over the components in the GForge NEXT platform. The chat bot can read messages in real-time, it follows through the conversation of the users. For example, whenever users are discussing about some issues with project progress, or talk about a new feature to be implemented, they can directly create a ticket from the terminal using a command like `/ticket summary:'calendar integration'`. Similarly, they can update the prirority of a ticket using a command like`/update priority:1 id:27519` or update the summary like `/update summary:'changed to new' id:27519`

### Creation of tickets:

![Tags](https://cloud.githubusercontent.com/assets/16812117/18616051/b60e96e2-7d7a-11e6-9eab-e8322001ce98.png)


Similarly we can obtain details of all users involved in the project.

### Getting detais of all users involved in a project:

![Tags](https://cloud.githubusercontent.com/assets/16812117/18616080/44ebddd4-7d7b-11e6-940b-18db7963dc7c.png)

### Sending chat message to any forumThread:

While in a forum thread, we can even send chat message to any other forumThread as shown below.

![Tags](https://cloud.githubusercontent.com/assets/16812117/18616123/d66a4930-7d7b-11e6-872a-227aa279c001.PNG)

### Searching StackOverflow:

Our chat bot integrates GForce NEXT API to StackExchange API. So, it's possible for users to directly search for some problem like an error. This can be invoked using commands like `search python` or `search overflowError` 

![Tags](https://cloud.githubusercontent.com/assets/16812117/18616203/c475a91c-7d7c-11e6-9686-17e64e9eabca.PNG)

### Getting directions using Google Maps:

If users talk about lunch or dinner at some location, our chat bot can give them directions to go using Google Maps API.

`How about we do our dinner at Memorial Union, Ames`

`Let us go to lunch at Hickory park, Ames`

![Tags](https://cloud.githubusercontent.com/assets/16812117/18616220/22dc2f30-7d7d-11e6-8531-54dedd4e2a75.PNG)

### Sending text messages to phones:

Our chat-bot is connected to Twilio API, so users can directly send text messages directly to their phones.

`text '+18164567509' 'sms from chat'`

![Tags](https://cloud.githubusercontent.com/assets/16812117/18616325/6f62db18-7d7f-11e6-83c3-3f2fe4906196.PNG)

![Tags](https://cloud.githubusercontent.com/assets/16812117/18616334/9a84f178-7d7f-11e6-8857-cf58b7120598.png)

### Future work

This chat-bot makes the chat client of GForge NEXT platform powerful and more useful to the users. With the advancements in technologies like deep learning and natural language processing, We could further improve this bot take care of anything users want to do in the GForge NEXT platform, without leaving their chat boxes.


### References

[1]. https://next.gforge.com/#/

[2]. https://next.gforge.com/apidoc
