title: org.navitproject.navit

# org.navitproject.navit

[Google Play Store](https://play.google.com/store/apps/details?id=org.navitproject.navit)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
// Build fingerprint: 'google/hammerhead/hammerhead:6.0.1/MOB30H/2751534:user/release-keys'
// Revision: '11'
// ABI: 'arm'
// pid: 12359, tid: 12359, name: itproject.navit  >>> org.navitproject.navit <<<
// signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x6979c0f4
//     r0 9e0fa82c  r1 9e0fa848  r2 b3a82333  r3 6979c0f4
//     r4 9e0fa800  r5 9e0fa848  r6 b38f4e50  r7 b38f4c70
//     r8 9e0fa82c  r9 b38f526c  sl b38f4c84  fp b38f6ed0
//     ip 00000000  sp be807004  lr b38f091c  pc b38ede74  cpsr 90010010
// 
// backtrace:
//     #00 pc 00001e74  /data/app/org.navitproject.navit-1/lib/arm/libmap_binfile.so (setup_pos.isra.3+8)
//     #01 pc 00004918  /data/app/org.navitproject.navit-1/lib/arm/libmap_binfile.so (map_rect_get_item_binfile+244)
//     #02 pc 0002c318  /data/app/org.navitproject.navit-1/lib/arm/libnavit.so (map_rect_get_item+44)
//     #03 pc 000286bc  /data/app/org.navitproject.navit-1/lib/arm/libnavit.so (do_draw+728)
//     #04 pc 00018cc8  /data/app/org.navitproject.navit-1/lib/arm/libnavit.so (callback_call+680)
//     #05 pc 00018e24  /data/app/org.navitproject.navit-1/lib/arm/libnavit.so (callback_call_args+84)
//     #06 pc 000011a0  /data/app/org.navitproject.navit-1/lib/arm/libgraphics_android.so (event_android_handle_timeout+16)
//     #07 pc 0005b25c  /data/app/org.navitproject.navit-1/lib/arm/libnavit.so (Java_org_navitproject_navit_NavitTimeout_TimeoutCallback+104)
//     #08 pc 000bb7eb  /data/app/org.navitproject.navit-1/oat/arm/base.odex (offset 0x88000)

```



