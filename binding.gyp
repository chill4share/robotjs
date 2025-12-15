{
  'targets': [{
    'target_name': 'robotjs',

    'dependencies': [
      '<!(node -p "require(\'node-addon-api\').gyp")',
    ],

    'include_dirs': [
      '../node-addon-api',
	  './src'
    ],

    'cflags!': [ '-fno-exceptions' ],
    'cflags_cc!': [ '-fno-exceptions' ],

    'xcode_settings': {
      'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
      'CLANG_CXX_LIBRARY': 'libc++',
      'MACOSX_DEPLOYMENT_TARGET': '10.7',
      'OTHER_CFLAGS': [ '-arch x86_64', '-arch arm64' ],
      'OTHER_LDFLAGS': [ '-arch x86_64', '-arch arm64' ]
    },

    'msvs_settings': {
      'VCCLCompilerTool': { 'ExceptionHandling': 1 },
    },

    'conditions': [
      ['OS == "mac"', {
        'include_dirs': [
          'System/Library/Frameworks/CoreFoundation.Framework/Headers',
          'System/Library/Frameworks/Carbon.Framework/Headers',
          'System/Library/Frameworks/ApplicationServices.framework/Headers',
          'System/Library/Frameworks/OpenGL.framework/Headers',
        ],
        'link_settings': {
          'libraries': [
            '-framework Carbon',
            '-framework CoreFoundation',
            '-framework ApplicationServices',
            '-framework OpenGL'
          ]
        }
      }],

      ['OS == "linux"', {
        'link_settings': {
          'libraries': [ '-lpng', '-lz', '-lX11', '-lXtst' ]
        },
        'sources': [
          '<(module_root_dir)/src/xdisplay.c'
        ]
      }],

      ["OS=='win'", {
        'defines': ['IS_WINDOWS'],
        'sources': [
          '<(module_root_dir)/src/Windows/keypress_win.c',
          '<(module_root_dir)/src/Windows/mouse_win.c',
          '<(module_root_dir)/src/Windows/screen_win.c'
        ]
      }]
    ],

    'sources': [
      '<(module_root_dir)/src/robotjs.cc',
      '<(module_root_dir)/src/deadbeef_rand.c',
      '<(module_root_dir)/src/mouse.c',
      '<(module_root_dir)/src/keypress.c',
      '<(module_root_dir)/src/keycode.c',
      '<(module_root_dir)/src/screen.c',
      '<(module_root_dir)/src/screengrab.c',
      '<(module_root_dir)/src/snprintf.c',
      '<(module_root_dir)/src/MMBitmap.c'
    ]
  }]
}
