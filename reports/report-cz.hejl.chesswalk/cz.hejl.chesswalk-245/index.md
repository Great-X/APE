title: cz.hejl.chesswalk

# cz.hejl.chesswalk

[Google Play Store](https://play.google.com/store/apps/details?id=cz.hejl.chesswalk)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
// Build fingerprint: 'google/hammerhead/hammerhead:6.0.1/MOB30H/2751534:user/release-keys'
// Revision: '11'
// ABI: 'arm'
// pid: 5968, tid: 6052, name: AsyncTask #5  >>> cz.hejl.chesswalk <<<
// signal 11 (SIGSEGV), code 2 (SEGV_ACCERR), fault addr 0x18378044
//     r0 001e19a3  r1 00000023  r2 00018434  r3 18378040
//     r4 9e718000  r5 9e718000  r6 00000001  r7 9e730464
//     r8 9e718010  r9 00000067  sl b3a343b0  fp 0000000a
//     ip 000cb7e8  sp 9d540160  lr b3a211a1  pc b3a21182  cpsr 200a0030
// 
// backtrace:
//     #00 pc 00005182  /data/app/cz.hejl.chesswalk-1/lib/arm/libchesswalk.so (_ZN5Board14genNonCapturesEPii+525)
//     #01 pc 00005ee9  /data/app/cz.hejl.chesswalk-1/lib/arm/libchesswalk.so (_ZN5Board16genAllLegalMovesEPii+20)
//     #02 pc 00002341  /data/app/cz.hejl.chesswalk-1/lib/arm/libchesswalk.so (_ZN6Engine9alphaBetaEP5Boardiiiiib+124)
//     #03 pc 00002581  /data/app/cz.hejl.chesswalk-1/lib/arm/libchesswalk.so (_ZN6Engine9alphaBetaEP5Boardiiiiib+700)
//     #04 pc 000023f9  /data/app/cz.hejl.chesswalk-1/lib/arm/libchesswalk.so (_ZN6Engine9alphaBetaEP5Boardiiiiib+308)
//     #05 pc 000023f9  /data/app/cz.hejl.chesswalk-1/lib/arm/libchesswalk.so (_ZN6Engine9alphaBetaEP5Boardiiiiib+308)
//     #06 pc 000023f9  /data/app/cz.hejl.chesswalk-1/lib/arm/libchesswalk.so (_ZN6Engine9alphaBetaEP5Boardiiiiib+308)
//     #07 pc 00002655  /data/app/cz.hejl.chesswalk-1/lib/arm/libchesswalk.so (_ZN6Engine6searchEP5Boardiib+148)
//     #08 pc 00002023  /data/app/cz.hejl.chesswalk-1/lib/arm/libchesswalk.so (Java_cz_hejl_chesswalk_OfflineGame_getBestMove+58)
//     #09 pc 0004c11f  /data/app/cz.hejl.chesswalk-1/oat/arm/base.odex (offset 0x33000)

```



