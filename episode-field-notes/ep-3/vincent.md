# Vincent Warmerdam, Episode 3 field notes

Vincent Warmerdam is an engineer at [marimo](https://marimo.io/) who has worked with Matt and Ines on spaCy and with [Rasa](https://rasa.com/). His segment centered on notebooks as interactive canvases for humans and agents: widget-driven exploration, agent-readable docs, Marimo Pair, cloud sandboxes, and the discipline of staying personally engaged instead of outsourcing understanding to the model.

## On working with agents

### What he loves: daydreams that become artifacts quickly

Vincent likes agents because they let small creative ideas become concrete fast enough to keep the idea alive. The Game of Life widget was his example: an asynchronous front-end and Python loop started as a "what if" and became something explorable. *"I do like the fact that they allow me to dream during the day a bit differently. So if I have a brain fart, it's a lot easier for that brain fart to be satisfied within half an hour."* [\[01:31:01\]](https://youtube.com/live/ud2WzkKeDZs?t=5461)

The creative unlock is not just speed, it is speed that leaves a usable artifact behind: *"So the fact that an agent allows me to sort of quickly bootstrap things like that, that's like a huge creative unlock."* [\[01:31:28\]](https://youtube.com/live/ud2WzkKeDZs?t=5488)

### What he finds most frustrating: hype that blocks calm learning

Vincent's frustration is less with agents themselves than with the media layer around them. When he wants to learn what [Hermes](https://hermes-agent.nousresearch.com/) is, he wants a calm, time-respectful explanation, not guru posture and algorithmic spectacle. *"The hype around it, it's, it's, oh God, I just want normal boring people to exchange notes, but instead you get all these, God, like, I don't know."* [\[01:32:09\]](https://youtube.com/live/ud2WzkKeDZs?t=5529)

His preferred norm is ordinary practitioners comparing notes: *"There is something about the way that ideas are being shared where it almost feels like you have to pretend to be a guru instead of being like a boring person that just says, I tried a bunch of stuff. It kind of works."* [\[01:32:20\]](https://youtube.com/live/ud2WzkKeDZs?t=5540)

## Skills

### [Marimo Pair](https://marimo.io/blog/marimo-pair)

Vincent showed Marimo Pair as an agent-notebook pairing skill, first with a simple slider. The key feature is that the agent can read Python variables and interact with UI elements in the notebook, instead of debugging through command-line prints. *"this is the new Marimo Pair thing. It's effectively a skill."* [\[01:24:25\]](https://youtube.com/live/ud2WzkKeDZs?t=5065)

The concrete demo was deliberately simple: ask the agent the slider value, then ask it to move the slider. *"It can read every single Python variable here, but you can also ask it to interact with UI elements."* [\[01:25:36\]](https://youtube.com/live/ud2WzkKeDZs?t=5136)

## Workflows

### Treat the notebook as a shared canvas

Vincent's core workflow is to make the notebook a space where both human and agent can manipulate live objects, inspect state, and learn by changing things. Wiggly Stuff widgets, Marimo Pair, and cloud sandboxes all serve that larger goal. *"We can really look at the notebook more like a canvas, and that's, think, where the quote came from, than before, because it's definitely more about having agents be able to interact with something that you yourself can also interact with."* [\[01:12:41\]](https://youtube.com/live/ud2WzkKeDZs?t=4361)

### Build libraries as Lego bricks for agents

Wiggly Stuff is designed as small composable widgets, with docs that agents can read. Vincent frames this as more useful than another instruction file when the library itself contains examples and conventions the model can imitate. *"the really nice philosophy with this Wiggly Stuff library is it's just a Lego brick and you can click it together with the rest of your code."* [\[01:11:45\]](https://youtube.com/live/ud2WzkKeDZs?t=4305)

That componentization makes the library agent-friendly: *"if you have a library full of Lego bricks that have this rule on how things should click together, it's a lot easier for Claude or whatever agent to figure out what the next Lego brick should be because there's examples to follow."* [\[01:23:04\]](https://youtube.com/live/ud2WzkKeDZs?t=4984)

### Use Conductor workspace scripts to make review loops automatic

Vincent uses Conductor as a wrapper around Codex, Claude, or terminal-based coding agents. The small but important trick is scripting workspace setup and demo-running through `conductor.json`, so every iteration can be reviewed in the browser without redoing setup. *"I can actually script this conductor.json thing."* [\[01:21:54\]](https://youtube.com/live/ud2WzkKeDZs?t=4914)

The run command opens all the demo notebooks, which makes visual checking cheap: *"whenever it's done an iteration, I can just open the notebook and see if it did the right thing."* [\[01:22:25\]](https://youtube.com/live/ud2WzkKeDZs?t=4945)

### Prefer fast, slightly worse models when they keep you engaged

Vincent argues that the best model can seduce the user into taking a back seat. A faster, "dumber" model may produce better human-agent collaboration because the human stays alert and in the loop. *"if you use a worse model, besides the fact that it's like actually a whole lot quicker usually, you have to be on your toes a little bit more."* [\[01:20:23\]](https://youtube.com/live/ud2WzkKeDZs?t=4823)

The speed matters because long waits trigger context switching: *"if there's a delay of like a minute, you're gonna do something else."* [\[01:20:32\]](https://youtube.com/live/ud2WzkKeDZs?t=4832)

### Start from scratch sometimes to avoid intellectual laziness

Vincent explicitly warns against letting the model do all the work. Even if an agent can produce the artifact, the human still needs the ability to build from first principles. *"there is a risk of intellectual laziness if you just have the L and really do everything."* [\[01:19:47\]](https://youtube.com/live/ud2WzkKeDZs?t=4787)

His prescription is tactile as well as conceptual: *"it is also good to be able to start from scratch yourself. Like there's something very empowering where you can just sort of say, screw it, I'm just building this from scratch."* [\[01:19:34\]](https://youtube.com/live/ud2WzkKeDZs?t=4774)

## Tools / projects he showed

### [Wiggly Stuff](https://koaning.github.io/wigglystuff/)

Wiggly Stuff is Vincent's side library of interactive Python notebook widgets. He showed widgets for 3D, graphs, painting, and Conway's Game of Life, all designed to work in notebooks and also in notebooks running fully in Wasm. *"I maintain this library on the side that basically has all of these widgets that are suspiciously useful, and it feels weird that people are sleeping on this."* [\[01:11:28\]](https://youtube.com/live/ud2WzkKeDZs?t=4288)

The docs are deliberately agent-readable: *"every single widget, the docs are also fully available in Markdown as well on the site."* [\[01:11:52\]](https://youtube.com/live/ud2WzkKeDZs?t=4312)

### Wiggly Stuff Paint widget and Game of Life demo

Vincent showed a notebook-native paint widget, then used a timer so Python could draw flowers over black pixels in the front end. He then swapped the playful flower example for an interactive Game of Life demo where drawing different shapes changes the simulated behavior. *"I'm able to interact with the game of life here."* [\[01:15:52\]](https://youtube.com/live/ud2WzkKeDZs?t=4552)

The pedagogical point is that interactivity makes the concept easier to understand: *"if I draw a straight line, then a lot of life starts to appear. But if I just draw an arc, it's going to be less life. Okay. Why is that?"* [\[01:15:57\]](https://youtube.com/live/ud2WzkKeDZs?t=4557)

### [remember.cards](https://remember.cards/)

Vincent showed remember.cards, a flashcard app he built and uses. The agent-related lesson came from asking an LLM to generate flashcards for saying "thank you" in many languages. It produced a useless English card, revealing the gap between generating plausible content and understanding the learner's goal. *"So I made it very hard to forget. So it's called remember.cards. And it's free, so people can go ahead and play with it."* [\[01:16:57\]](https://youtube.com/live/ud2WzkKeDZs?t=4617)

The failure case was the lesson: *"The first card of the entire deck was, how do you say thank you in English? And you would flip the card and it would say thank you."* [\[01:17:39\]](https://youtube.com/live/ud2WzkKeDZs?t=4659)

### [Conductor](https://www.conductor.build/)

Vincent uses Conductor to run coding-agent workspaces, with a disclosure that he has a working relationship with the company. In his setup, Conductor wraps Codex, Claude, or terminal agents and gives each conversation its own workspace. *"I like to use this thing called Conductor. And there's other apps like it."* [\[01:21:20\]](https://youtube.com/live/ud2WzkKeDZs?t=4880)

The useful feature is repeatable setup and review through `conductor.json`: install commands, run commands, and browser-opened notebook demos. *"it's like a little thing that that's just always there and I don't have to think about setting this up."* [\[01:22:28\]](https://youtube.com/live/ud2WzkKeDZs?t=4948)

### [Marimo Pair](https://marimo.io/blog/marimo-pair)

Marimo Pair connects a notebook to a coding agent so the agent can read variables, write into a scratchpad, and interact with UI elements. Vincent used OpenCode and a Kimi model in the demo, but emphasized that the idea works with Claude, Codex, or another coding agent. *"you can do this with Claude, you can do this with Codex, you can do this with whatever, Slider value is 3."* [\[01:25:26\]](https://youtube.com/live/ud2WzkKeDZs?t=5126)

The debug benefit is direct access to state: *"you just have a way to give Claude or whatever access to every single Python variable. And that really lets it fix its own problems way better than anything you can print to the command line effectively."* [\[01:26:30\]](https://youtube.com/live/ud2WzkKeDZs?t=5190)

### [MoLab](https://molab.marimo.io/)

Vincent described MoLab as a cloud sandbox product for Marimo notebooks, with an announcement expected soon. He did not demo the unreleased feature, but framed it as "Colab, but it uses Marimo." *"all the code will actually be running in the cloud in the sandbox for you."* [\[01:27:29\]](https://youtube.com/live/ud2WzkKeDZs?t=5249)

### [Pi](https://pi.dev/docs/latest/extensions)

Vincent showed Pi as a TypeScript-based agent customization surface that can listen for tool-call events and restrict what the agent can read. In the Marimo sandbox case, the goal is to let a local terminal agent connect to cloud execution while preventing it from touching local files except the specific Marimo Pair files it needs. *"If the tool call is of type read, then you can say you're only allowed to read the Marimo Pair files because everything else has to happen in the cloud."* [\[01:28:08\]](https://youtube.com/live/ud2WzkKeDZs?t=5288)

The point is a bespoke coding agent with much narrower permissions: *"You can really narrow down what Pi is allowed to touch."* [\[01:28:21\]](https://youtube.com/live/ud2WzkKeDZs?t=5301)

### [Calm Code](https://calmcode.io/)

Hugo closed the segment by pointing people to Vincent's Calm Code. Vincent tied this to his wider theme of calm, boring, non-hype learning. *"sometimes you want to follow the boring person, not the person with like the ridiculous freaking thumbnail."* [\[01:35:39\]](https://youtube.com/live/ud2WzkKeDZs?t=5739)

## Explainers

### LLMs can think without understanding

The remember.cards example was Vincent's cleanest distinction between generation and understanding. The model could generate plausible cards for many languages, but it could not infer that "thank you" in English is a useless card for him. *"that's a perfect example for me where the LLM can do thinking, but it cannot do understanding."* [\[01:17:51\]](https://youtube.com/live/ud2WzkKeDZs?t=4671)

That distinction changes how he uses agents: *"the goal is that I understand something, writing flashcards, I tend to do that by hand still, because that helps me also remember better."* [\[01:17:58\]](https://youtube.com/live/ud2WzkKeDZs?t=4678)

### Interactivity turns explanations into understanding

Vincent argues that agents explaining code is weaker than agents giving you something you can manipulate. If the agent wants to teach a multi-step concept, the user learns more by reading code, changing it, and seeing feedback. *"something about reading the code and being able to change the code to see what happens makes me better at understanding the thing than if I were just to read it from a book."* [\[01:16:39\]](https://youtube.com/live/ud2WzkKeDZs?t=4599)

His preferred medium is not passive content: *"I prefer to have something of a canvas that also gives me feedback than if I were just to passively sit here and watch content and pretend that that's something that actually teaches me anything."* [\[01:18:25\]](https://youtube.com/live/ud2WzkKeDZs?t=4705)

### Component shape can matter more than another skill file

Vincent's Wiggly Stuff and scikit-learn comparison turns "agent readiness" into API design. If components are small, consistent, documented, and easy to test, the model can infer the next component from the existing pattern. *"if you have a library that you can get into this mold, that will do more than any scale file, I think, because you get into the situation where the LLM can just fix its own problems."* [\[01:23:31\]](https://youtube.com/live/ud2WzkKeDZs?t=5011)

### Direct variable access changes agent debugging

Marimo Pair removes a debugging loop that Vincent sees as wasteful: printing intermediate values to the command line, inspecting column names, then repeating across pipeline steps. A notebook pairing surface gives the agent access to the live Python state directly. *"there's like a five-step pipeline. Let me print all those separate steps to figure out what the column names are. All those things basically go away because you just have a way to give Claude or whatever access to every single Python variable."* [\[01:26:23\]](https://youtube.com/live/ud2WzkKeDZs?t=5183)

He also points toward richer object representations as agent instruction manuals: *"you could also imagine that this becomes like the instruction manual for the agent on how to actually work with this variable if you have very custom objects."* [\[01:26:53\]](https://youtube.com/live/ud2WzkKeDZs?t=5213)

### Sandboxing is only meaningful with a real sandbox

Vincent is careful about the limits of permission controls. Restricting which files a skill can read is not enough if the local notebook still has disk access. The sandboxing story works best when execution actually happens in a proper cloud sandbox. *"this only works if you have a very proper sandbox at the moment."* [\[01:30:15\]](https://youtube.com/live/ud2WzkKeDZs?t=5415)

The broader warning is about casually importing skills and files: *"people just randomly start pulling in all sorts of files and skills, not check it out, and that that's going to lead to all sorts of big problems."* [\[01:30:26\]](https://youtube.com/live/ud2WzkKeDZs?t=5426)

### Weather alchemy and AI hype

Vincent used 1800s weather prediction as a historical analogy for AI hype. When demand is high enough, bad supply finds a market, including alchemists and quacks. The way out is boring empirical work. *"it's because the demand for something was so high that bullshit supply suddenly had like a reason to actually exist and survive for a bit there."* [\[01:34:30\]](https://youtube.com/live/ud2WzkKeDZs?t=5670)

The conclusion is a call for slower, calmer practice: *"The internet could use a good linter. Yeah, I'm inclined to agree. But anyway, but also like for yourself, it's okay to go slow if it means you understand it better."* [\[01:35:23\]](https://youtube.com/live/ud2WzkKeDZs?t=5723)

## Additional quotations

- On interactive widgets as a missing notebook affordance: *"the thing that was missing inside of my notebook was a lack of interactivity."* [\[01:13:05\]](https://youtube.com/live/ud2WzkKeDZs?t=4385)
- On the purpose of notebooks: *"The whole point of a notebook is that I eventually understand something and that's not something the agent can do for me."* [\[01:13:56\]](https://youtube.com/live/ud2WzkKeDZs?t=4436)
- On interactive charts: *"if the chart is also interactive, you tend to learn way quicker."* [\[01:14:16\]](https://youtube.com/live/ud2WzkKeDZs?t=4456)
- On agent-readable docs: *"OpenCode should also be able to figure out how this library works and how the Lego bricks click together, if it were."* [\[01:12:25\]](https://youtube.com/live/ud2WzkKeDZs?t=4345)
- On a small but useful workspace habit: *"when a workspace sets up, I want you to run this one install command."* [\[01:22:03\]](https://youtube.com/live/ud2WzkKeDZs?t=4923)
- On Marimo Pair and UI manipulation: *"I'm gonna not touch the keyboard anymore. And you should see the slider jump any moment now."* [\[01:25:43\]](https://youtube.com/live/ud2WzkKeDZs?t=5143)
- On agent safety and skill files: *"it remains a file, and it remains the fact that you give that to an agent. So be careful where you get that file from, and make sure it's not tampered with as you download it."* [\[01:30:37\]](https://youtube.com/live/ud2WzkKeDZs?t=5437)
- On calm learning: *"Don't choose the life of imitation, but it's all that I'm seeing if it sometimes feels like."* [\[01:34:53\]](https://youtube.com/live/ud2WzkKeDZs?t=5693)
