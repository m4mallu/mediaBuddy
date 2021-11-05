<h1 align="left">
    <a target="_blank">
        MediaBuddy
        <img src="https://loading.io/assets/img/c/icon/search.svg" width="40px" style="max-width:100%;">
    </a>
</h1>

#### A Telegram Inline media searching robot without any database.
<br>

<details>
    <summary><b>About</b></summary>
    <p align="left"></p>
        <a target="_blank">
            <img src="https://c.tenor.com/rec5dlPBK2cAAAAd/mr-bean-waiting.gif" width="300px" />
    </a>

    mediaBuddy is an inline media searching robot. If you have so many movie channels and you are searching for a 
    particular movie in each and everywhere and spending your valuable time in this process, the bot is yours.
    The bot can search inline in your movie chats and also can provide a link to your queried one, thus you can 
    easily access the required media. Your perfect media buddy.

</details>
<details>
    <summary><b>Working</b></summary>
    <p align="left"></p>

        🔷 When bot is deployed with a user session string, it will find all the groups and channels of the user.
        🔷 From the above, it sorts the movies channels and groups and make a master list for searching your queries.
        🔷 When you search a keyword as inline, the bot will search the same in the master list and gives the output.
        🔷 The output will be the file name with a hyper link to the original file.
        🔷 By clicking, you can easily migrate to the file location thus saves your valuable time in searching.
</details>
<details>
    <summary><b>What to do</b></summary>
    <p align="left"></p>

        🔷 Make an inline bot with Telegram Botfather.
        🔷 Deploy the bot local pc, VPS or in heroku.
        🔷 Join some movie channels.
        🔷 Search movies inline.
</details>
<details>
    <summary><b>Mandatory Variables</b></summary>
    <p align="left"></p>
    
    🔷 API_HASH        -   Your API Hash, get it from my.telegram.org
    🔷 APP_ID          -   Your APP ID, get it from my.telegram.org 
    🔷 BOT_TOKEN       -   Your bot token, get it from @BotFather
    🔷 TG_USER_SESSION -   Your session string (Generate for 'User', dont use any bot session)
</details>
<details>
    <summary><b>Generate User Session</b></summary>
    <p align="left"></p>
    <a href="https://replit.com/@ayrahikari/pyrogram-session-maker">
        <img src="https://img.shields.io/badge/Generate-String%20Session-orange" height="30" />
</a>
    <ul>
        <li>Open the above link and start the application.</li>
        <li>Give your APP_ID, API_HASH - Get it from <a href="https://my.telegram.org/auth"><b>HERE</b></a> </li>
        <li>On the next step, select <code>1 = User Bot</code> option .</li>
        <li>Give your phone number in <a href="https://www.cm.com/blog/how-to-format-international-telephone-numbers/">international format</a> .</li>
        <li>Give the OTP and Auth Phrase if any</li>
        <li>This will get your long user session string</li>
        <li><a href="https://docs.pyrogram.org/topics/storage-engines?highlight=string%20sessions#session-strings"><b>Keep the String safe, anyone can access your account using it.</b></a></li>
    </ul>
</details>
<details>
    <summary><b>@BotFather Commands</b></summary>
    <p align="left">
    
    start - Check Alive                     Usage: /start
    view   - Vire the currents chats        Usage: /viewchats
    update - Add a chat to the list         Usage: /update -100xxxxxxxxxx
    delete - Remove chats from the list     Usage: /remove -100xxxxxxxxxx
</details>
<details>
    <summary><b>Deploy in VPS</b></summary>
    <p align="left">
    <ul>
        <li>Create a <code>config.py</code> file with the Mandatory Variables mentioned above.</li>
        <li>Refer <code>sample_config.py</code> for creating <code>config.py</code> file. don't miss any parameters</li>
        <li>Open terminal and run the following commands.</li>
        <li><code>git clone https://github.com/m4mallu/mediaBuddy</code></li>
        <li><code>cd mediaBuddy</code></li>
        <li>Save the <code>config.py</code> file in side the current working directory cloned.</li>
        <li>Run the below commands in the same terminal window.</li>
    </ul>

    virtualenv -p python3 venv
    . ./venv/bin/activate
    pip3 install -r requirements.txt
    python3 main.py
</details>
<details>
    <summary><b>Deploy Heroku</b></summary>
    <p align="left">
        <a href="https://heroku.com/deploy?template=https://github.com/m4mallu/mediaBuddy">
     <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
  </a></p>
</details>
<details>
    <summary><b>Limitations</b></summary>
    <p align="left">
    <ul>
        <li>Presently <code>document</code> type is only supported.</li>
        <li>Chance for getting heavy FloodWaits in <code>searchMessages</code> in case of massive number of media chats.</li>
    </ul>
</details>
<details>
    <summary><b>Developer</b></summary>
    <p align="left">
        <img alt="GPL3" src ="https://c.tenor.com/10Zdx_RXqgcAAAAC/programming-crazy.gif" width="260px" style="max-width:100%;"/><br>
            <a href="https://t.me/space4renjith"><b>Renjit Mangal</b></a> &nbsp;|&nbsp;
                <a href="https://t.me/rmprojects"><b>Update Channel</b></a>
    </p>
</details>
<details>
    <summary><b>Donate</b></summary>
    <p align="left"><br>
    <b>Buy me a coffee for the work !</b><br>
    <img src="https://telegra.ph/file/b926b7e8ea84826d81d8a.png" width="260px" style="max-width:100%;"/><br><br>
      <a href="https://www.paypal.me/space4renjith" target="_blank">
        <img src="https://img.shields.io/badge/Donate-Me-blueviolet?style=for-the-badge&logo=paypal">
    </a>
</p>
</details>
<details>
    <summary><b>Credits</b></summary>
    <p align="left">
        <a href="https://github.com/pyrogram/pyrogram"><b>Pyrogram</b></a>
    </p>
</details>
<details>
    <summary><b>Licence</b></summary>
    <p align="left">
        <a href="https://choosealicense.com/licenses/gpl-3.0/">
            <img alt="GPL3" src ="https://telegra.ph/file/dd47727c24b7e7384a760.png" width="150" height="150"/>
        </a>
    </p>
</details>
<p align="center">
    <a href="https://t.me/space4renjith">
        <img alt="GPL3" src ="https://telegra.ph/file/c4f778ccfc576a954dd20.gif" width="340" height="214"/>
    </a>
</p>
