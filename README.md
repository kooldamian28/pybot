# pybot
A python bot that can automatically send specific messages when triggered.
The bot ("bot.py") reads the text message from the file: "file.txt" and automatically types it and presses enter on your keyboard to send it.
You can bookmark <a href="https://kooldamian28.github.io/pybot/">this page</a> also for easy reference: <a href="https://kooldamian28.github.io/pybot/">kooldamian28.github.io/pybot/</a>

## Instructions
1. Enter your personal message in "file.txt"
2. Run the "bot.py"
3. Click on the text field you want the bot to type in.

## More info
The bot is programmed to wait for 5 seconds before typing, if you want to adjust the delay, go to line 2 or the line which says "time.sleep(5)" and enter the time in seconds between the brackets. In the format as, time.sleep(seconds), where "seconds" is the time in seconds.

In line 4 you can adjust the bot to open any file you want, in the format, a = open("anyfile"), where "anyfile" is the file you want to open.

# Notice
The license that I used for this project is <a href="https://opensource.org/licenses/BSD-3-Clause">The BSD-3-Clause</a>, as a result, by using this software you agree with the Terms, Conditions and Limitations of the <a href="https://opensource.org/licenses/BSD-3-Clause">license</a>. 

**IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.**
