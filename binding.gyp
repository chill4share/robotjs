{
  'targets': [{
    'target_name': 'robotjs',

    'dependencies': [
      '<(module_root_dir)/../../../node-addon-api/src/node_api.gyp:nothing'
    ],

    'include_dirs': [
      '<(module_root_dir)/../../../node-addon-api'
    ],

    'cflags!': [ '-fno-exceptions' ],
    'cflags_cc!': [ '-fno-exceptions' ],
    'xcode_settings': {
      'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
      'CLANG_CXX_LIBRARY': 'libc++',
      'MACOSX_DEPLOYMENT_TARGET': '10.7',
      'OTHER_CFLAGS': [
        '-stdlib=libc++',
        '-mmacosx-version-min=10.7'
      ]
    },
    'msvs_settings': {
      'VCCLCompilerTool': {
        'ExceptionHandling': 1
      }
    },
    'conditions': [
      ['OS=="mac"', {
        'sources': [
          'src/robotjs.cc',
          'src/deadbeef_rand.c',
          'src/mouse.c',
          'src/keypress.c',
          'src/keycode.c',
          'src/screen.c',
          'src/screengrab.c',
          'src/snprintf.c',
          'src/MMBitmap.c',
          'src/Mac/keypress_osx.mm',
          'src/Mac/mouse_osx.mm',
          'src/Mac/screen_osx.mm'
        ]
      }],
      ['OS=="win"', {
        'sources': [
          'src/robotjs.cc',
          'src/deadbeef_rand.c',
          'src/mouse.c',
          'src/keypress.c',
          'src/keycode.c',
          'src/screen.c',
          'src/screengrab.c',
          'src/snprintf.c',
          'src/MMBitmap.c',
          'src/Windows/keypress_win.c',
          'src/Windows/mouse_win.c',
          'src/Windows/screen_win.c'
        ],
        'libraries': [
          '-lgdi32',
          '-luser32'
        ]
      }],
      ['OS=="linux"', {
        'sources': [
          'src/robotjs.cc',
          'src/deadbeef_rand.c',
          'src/mouse.c',
          'src/keypress.c',
          'src/keycode.c',
          'src/screen.c',
          'src/screengrab.c',
          'src/snprintf.c',
          'src/MMBitmap.c',
          'src/X11/keypress_x11.c',
          'src/X11/mouse_x11.c',
          'src/X11/screen_x11.c'
        ],
        'libraries': [
          '-lX11',
          '-lXtst'
        ]
      }]
    ],
    'sources': [
      'src/robotjs.cc',
      'src/deadbeef_rand.c',
      'src/mouse.c',
      'src/keypress.c',
      'src/keycode.c',
      'src/screen.c',
      'src/screengrab.c',
      'src/snprintf.c',
      'src/MMBitmap.c'
    ]
  }]
}
