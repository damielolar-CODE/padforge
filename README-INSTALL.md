# PadForge — install on your iPhone

This folder is a complete, ready-to-build Xcode project. **You do not need
Flutter, Homebrew, or the Terminal.** Everything PadForge needs is already
compiled into the `Frameworks` folder next to the project.

You need: a Mac with **Xcode** installed (free from the Mac App Store), a
**Lightning or USB-C cable**, and an **Apple ID**.

---

## 1. Unzip

Double-click `PadForge-iOS-Standalone.zip`. You get a folder called
`PadForge-iOS`. Move it somewhere sensible — your Documents folder is fine.
Don't leave it inside the Downloads "quarantine" if you can avoid it.

## 2. Open the project

Inside `PadForge-iOS`, double-click **`PadForge.xcodeproj`** (the blue
blueprint-looking icon). Xcode opens.

If Xcode asks to "install additional required components", say yes and let it
finish.

## 3. Tell Xcode who you are

1. In the left-hand column, click the **blue `PadForge` icon at the very top**
   (the project itself, not the folders below it).
2. In the middle of the window, under **TARGETS**, make sure **PadForge** is
   selected.
3. Click the **Signing & Capabilities** tab.
4. **Automatically manage signing** should already be ticked. Leave it ticked.
5. Open the **Team** dropdown and choose your name. If your Apple ID isn't
   listed, choose **Add an Account…**, sign in with your Apple ID, then come
   back and pick it from the dropdown.

If a red error appears saying the bundle identifier is already in use, change
**Bundle Identifier** from `com.padforge.app` to something unique, e.g.
`com.yourname.padforge`. The error clears once it's unique.

## 4. Plug in your iPhone and press Play

1. Connect the iPhone to the Mac with a cable. Unlock the phone and tap
   **Trust This Computer** if asked.
2. At the top of the Xcode window there's a dropdown that probably says
   something like *"Any iOS Device"*. Click it and choose **your iPhone** by
   name.
3. Press the **▶ (Play)** button at the top left.

The first build takes a couple of minutes. After that Xcode installs PadForge
on the phone and launches it.

## 5. Trust the app on the phone (first time only)

The very first launch will probably fail with *"Untrusted Developer"*. On the
iPhone:

**Settings → General → VPN & Device Management → (your Apple ID) → Trust**

Then tap the PadForge icon on the home screen, or press ▶ in Xcode again.

## 6. Allow the microphone

The first time you use the tape deck / looper, iOS asks for microphone access.
Tap **Allow** — recording will not work otherwise. (If you tap Don't Allow by
mistake: Settings → PadForge → Microphone.)

---

## Connecting the Akai MPD218

The MPD218 is a USB device, so it needs an adapter:

- **iPhone with a Lightning port:** *Lightning to USB 3 Camera Adapter*
- **iPhone with USB-C:** *USB-C to USB Adapter* (or any decent USB-C hub)

**Use the powered version if you can.** The Lightning to USB 3 Camera Adapter
has a second Lightning socket — plug a charger into it. The MPD218 draws more
current than an iPhone likes to supply on its own, and without external power
the pads may not light up or the phone may report "this accessory uses too much
power".

Plug the MPD218 in *before* opening PadForge, or use the refresh/reconnect
control in the app's MIDI settings. The pads should light up when it has power.

---

## A note about free Apple IDs — the 7-day thing

If you signed in with a **free** Apple ID (i.e. you are not paying for the
Apple Developer Program), the app is signed with a certificate that **expires
after 7 days**. After that PadForge will refuse to open ("app is no longer
available").

**The fix is simple: plug the phone back in, open the project, and press ▶
again.** That re-signs it for another 7 days. Nothing is lost — your kits and
recordings stay on the phone.

Other free-account limits worth knowing:
- You can have at most 3 apps installed this way at a time.
- You can register a limited number of devices per week.

A paid Apple Developer account ($99/year) extends the certificate to a year.

---

## If something goes wrong

**"Signing for PadForge requires a development team"**
You skipped step 3 — pick your name in the Team dropdown.

**"Unable to install… bundle identifier is not available"**
Change the Bundle Identifier as described in step 3.

**"Could not launch PadForge" / "Untrusted Developer"**
Do step 5 on the phone.

**The app installs but shows a black screen**
Make sure the whole `PadForge-iOS` folder was unzipped and kept together —
`PadForge.xcodeproj` and the `Frameworks` folder must sit side by side. Moving
the `.xcodeproj` on its own will break it.

**Xcode says the device is "not supported" or asks to download a Support File**
Your iPhone's iOS version is newer than your Xcode. Update Xcode from the Mac
App Store.

**The MPD218 isn't detected**
Check the adapter is a *camera/host* adapter (not a plain charging cable),
supply external power to it, and reconnect it before launching PadForge.
