#!/usr/bin/env python3
# Injects a release signingConfig (reading android/key.properties) into a
# Flutter-generated android/app/build.gradle.kts. Idempotent-ish; expects the
# stock template's `signingConfig = signingConfigs.getByName("debug")` line.
import re, sys
p = sys.argv[1]
s = open(p).read()
if "java.util.Properties" not in s:
    s = "import java.util.Properties\nimport java.io.FileInputStream\n" + s
if "val keystoreProperties" not in s:
    loader = (
        "\nval keystoreProperties = Properties()\n"
        'val keystorePropertiesFile = rootProject.file("key.properties")\n'
        "if (keystorePropertiesFile.exists()) {\n"
        "    keystoreProperties.load(FileInputStream(keystorePropertiesFile))\n"
        "}\n"
    )
    s = re.sub(r"\nandroid \{", loader + "\nandroid {", s, count=1)
    signing = (
        "\n    signingConfigs {\n"
        '        create("release") {\n'
        '            keyAlias = keystoreProperties["keyAlias"] as String\n'
        '            keyPassword = keystoreProperties["keyPassword"] as String\n'
        '            storeFile = file(keystoreProperties["storeFile"] as String)\n'
        '            storePassword = keystoreProperties["storePassword"] as String\n'
        "        }\n"
        "    }\n"
    )
    s = re.sub(r"android \{", "android {" + signing, s, count=1)
s = s.replace('signingConfig = signingConfigs.getByName("debug")',
              'signingConfig = signingConfigs.getByName("release")')
open(p, "w").write(s)
print("OK: signing injected into", p)
