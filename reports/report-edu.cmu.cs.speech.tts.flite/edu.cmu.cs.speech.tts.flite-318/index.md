title: edu.cmu.cs.speech.tts.flite

# edu.cmu.cs.speech.tts.flite

[Google Play Store](https://play.google.com/store/apps/details?id=edu.cmu.cs.speech.tts.flite)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
// Build fingerprint: 'google/hammerhead/hammerhead:6.0.1/MOB30H/2751534:user/release-keys'
// Revision: '11'
// ABI: 'arm'
// pid: 4084, tid: 4084, name: peech.tts.flite  >>> edu.cmu.cs.speech.tts.flite <<<
// signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x24
//     r0 00000000  r1 be826cf0  r2 79eb47ba  r3 b6ce7ec0
//     r4 00000000  r5 fffffffe  r6 00000000  r7 be826cb8
//     r8 be826cbc  r9 be826cc0  sl be826cf4  fp b0729290
//     ip be826cf0  sp be826ca8  lr 9d609ad5  pc 9d60b0ae  cpsr 600f0030
// 
// backtrace:
//     #00 pc 000140ae  /data/app/edu.cmu.cs.speech.tts.flite-1/lib/arm/libttsflite.so (_ZN11FliteEngine6Voices17IsLocaleAvailableENS_6StringES1_S1_+41)
//     #01 pc 00012ad1  /data/app/edu.cmu.cs.speech.tts.flite-1/lib/arm/libttsflite.so (_Z19isLanguageAvailablePvPKcS1_S1_+160)
//     #02 pc 000126d3  /data/app/edu.cmu.cs.speech.tts.flite-1/lib/arm/libttsflite.so (Java_edu_cmu_cs_speech_tts_flite_NativeFliteTTS_nativeIsLanguageAvailable+74)
//     #03 pc 0001561d  /data/app/edu.cmu.cs.speech.tts.flite-1/oat/arm/base.odex (offset 0x10000)

```



