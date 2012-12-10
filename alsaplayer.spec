%define major       0
%define libname     %mklibname %name %major
%define libnamedev     %mklibname -d %name
%define build_flac 1

Name:		alsaplayer
Summary:	Advanced Linux Sound Architecture (ALSA) player
Version: 0.99.81
Release: 1
Source:		http://www.alsaplayer.org/%name-%version.tar.bz2
Source1:	%name-icons.tar.bz2
URL:		http://www.alsaplayer.org/
License:	GPLv3+

Group:		Sound
BuildRequires:  pkgconfig(alsa)  
BuildRequires:  pkgconfig(esound)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  libmikmod-devel 
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(jack) >= 0.70.4
BuildRequires:  libnas-devel
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  libxosd-devel

Requires: 	%{name}-plugin-ui-gtk
ExcludeArch:	sparc sparc64
Obsoletes: alsaplayer-plugin-read-curl
Provides: alsaplayer-plugin-read-curl

%description
Advanced Linux Sound Architecture (ALSA) utils. Modularized architecture with
support for a large range of ISA and PCI cards. Fully compatible with OSS/Lite
(kernel sound drivers), but contains many enhanced features.

%package -n %libname
Summary:    AlsaPlayer sharedlibrary
Group:      System/Libraries
Provides: libalsaplayer
Obsoletes: libalsaplayer

%description -n %libname
This is the shared librairy of AlsaPlayer.

%package -n %libnamedev
Summary:    AlsaPlayer devel stuff 
Group:      Development/C
Requires: %libname = %version
Provides: libalsaplayer-devel = %version-%release
Obsoletes: %mklibname -d alsaplayer 0

%description -n %libnamedev
This is the development part of the AlsaPlayer librairy. 


%if %build_flac
%package plugin-input-flac
Summary:    AlsaPlayer plugin for playing FLAC audio files
Group:		Sound
Requires: alsaplayer => %version-%release
BuildRequires: liboggflac-devel
%description plugin-input-flac
This plugin enables alsaplayer to play files in the lossless audio 
compression format FLAC.
%endif

%package plugin-input-mod
Summary:    AlsaPlayer plugin for playing MOD modules
Group:		Sound
Requires: alsaplayer => %version-%release

%package plugin-input-mad
Summary:    AlsaPlayer plugin
Group:		Sound
Requires: alsaplayer => %version-%release

%package plugin-input-sndfile
Summary:    AlsaPlayer plugin
Group:		Sound
Requires: alsaplayer => %version-%release

%package plugin-input-vorbis
Summary:    AlsaPlayer plugin
Group:		Sound
Requires: alsaplayer => %version-%release

%package plugin-output-jack
Summary:    AlsaPlayer for the jack sound server
Group:		Sound
Requires: alsaplayer => %version-%release

%package plugin-output-esound
Summary:    AlsaPlayer plugin
Group:		Sound
Requires: alsaplayer => %version-%release

%package plugin-output-nas
Summary:    AlsaPlayer NAS output plugin
Group:		Sound
Requires: alsaplayer => %version-%release


%package plugin-ui-gtk
Summary:    AlsaPlayer plugin
Group:		Sound
Requires: alsaplayer => %version-%release

%package plugin-scopes
Summary:    AlsaPlayer graphical scopes
Group:		Sound
Requires: alsaplayer => %version-%release, alsaplayer-plugin-ui-gtk

%description plugin-input-mod
This plugin enables alsaplayer to play module music files.
Supported file formats include MOD, STM, S3M, MTM, XM, ULT, and IT.

%description plugin-input-mad
This plugin enables alsaplayer to play mpeg files though the libmad library.
It currently supports MPEG-1 and the MPEG-2  extension to Lower Sampling
Frequencies, as well as the so-called MPEG 2.5 format. All three audio layers
(Layer I, Layer II, and Layer III a.k.a. MP3) are fully implemented.

%description plugin-input-sndfile
This plugin enables alsaplayer to play sound files such as AIFF, AU
and WAV files through the sndfile library. It can currently read 8,
16, 24 and 32-bit PCM files as well as 32-bit floating point WAV files
and a number of compressed formats.

%description plugin-input-vorbis
This plugin enables alsaplayer to play ogg vorbis music files.

%description plugin-output-jack
This plugin enables alsaplayer to play music with the jack daemon.

%description plugin-output-esound
This plugin enables alsaplayer to play music with the esound daemon.

%description plugin-output-nas
This plugin enables alsaplayer to play music with the NAS daemon.

%description plugin-ui-gtk
This plugin adds a nice graphical interface to alsaplayer.

%description plugin-scopes
This plugin adds some nice graphical visualization plugins (scopes).

%prep
%setup -q -n %name-%version

%build
%define _disable_ld_no_undefined 1
%configure2_5x --enable-alsa --enable-esd --disable-debug --enable-oggvorbis --enable-prefer-mad --disable-gtk --enable-gtk2
%make

%install
rm -rf %buildroot %name.lang
 %makeinstall_std
#clean unpackaged files:
rm -rf %buildroot%_datadir/doc/alsaplayer
rm -rf %buildroot%_libdir/%name/*/*.la


tar xfj %SOURCE1 -C %buildroot/%_datadir
# fix permissions:
chmod 755 docs/reference/html

%find_lang %name

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif


# TV: update me aka on each new upstream release, check for new plugins
%files -f %name.lang
%doc docs/*.txt
%doc COPYING
%_datadir/applications/*.desktop
%_bindir/*
%dir %_libdir/%name
%dir %_libdir/%name/*/
%_libdir/%name/input/libcdda.so
%_libdir/%name/input/libwav.so
%_libdir/%name/output/libalsa_out.so
%_libdir/%name/output/libnull_out.so
%_libdir/%name/output/liboss_out.so
%_libdir/%name/interface/libdaemon_interface.so
%_libdir/%name/interface/libtext_interface.so
%_libdir/%name/interface/libxosd_interface.so
%_libdir/%name/reader/libfile.so
%_libdir/%name/reader/libhttp.so
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_mandir/man1/%name.*

%files -n %libname
%doc COPYING
%_libdir/libalsaplayer.so.0.0.2
%_libdir/libalsaplayer.so.0

%files  -n %libnamedev
%doc COPYING
%doc docs/reference/html/
%_includedir/alsaplayer/
%_libdir/libalsaplayer.so
%_libdir/pkgconfig/alsaplayer.pc

%if %build_flac
%files plugin-input-flac
%doc COPYING
%_libdir/%name/input/libflac_in.so
%endif

%files plugin-input-mod
%doc COPYING
%_libdir/%name/input/libmod.so

%files plugin-input-mad
%doc COPYING
%_libdir/%name/input/libmad_in.so

%files plugin-input-sndfile
%doc COPYING
%_libdir/%name/input/libsndfile_in.so

%files plugin-input-vorbis
%doc COPYING
%_libdir/%name/input/libvorbis_in.so

%files plugin-output-jack
%doc COPYING
%_libdir/%name/output/libjack_out.so

%files plugin-output-esound
%doc COPYING
%_libdir/%name/output/libesound_out.so

%files plugin-output-nas
%doc COPYING
%_libdir/%name/output/libnas_out.so

%files plugin-ui-gtk
%doc COPYING
%_libdir/%name/interface/libgtk2_interface.so

%files plugin-scopes
%doc COPYING
%_libdir/%name/scopes2


%changelog
* Mon Nov 08 2010 Götz Waschk <waschk@mandriva.org> 0.99.81-1mdv2011.0
+ Revision: 595013
- new version
- fix source URL
- drop patches

* Tue Jun 16 2009 Jérôme Brenier <incubusss@mandriva.org> 0.99.80-3mdv2010.0
+ Revision: 386377
- fix str fmt

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 0.99.80-3mdv2009.0
+ Revision: 271774
- fix build
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 12 2007 Funda Wang <fwang@mandriva.org> 0.99.80-2mdv2008.1
+ Revision: 108192
- rebuild for new lzma

* Sun Nov 04 2007 Götz Waschk <waschk@mandriva.org> 0.99.80-1mdv2008.1
+ Revision: 105929
- new version
- drop patch

* Thu Oct 11 2007 Götz Waschk <waschk@mandriva.org> 0.99.80-0.rc4.1mdv2008.1
+ Revision: 97141
- new version

* Tue Oct 09 2007 Götz Waschk <waschk@mandriva.org> 0.99.80-0.rc3.1mdv2008.1
+ Revision: 96172
- new version

* Thu Jul 26 2007 Götz Waschk <waschk@mandriva.org> 0.99.80-0.rc2.1mdv2008.0
+ Revision: 55931
- new version
- drop patches 0,2
- update patch 1
- new devel package name
- update file list

  + Emmanuel Blindauer <blindauer@mandriva.org>
    - Removed ppc from archExclude: it build on ppc too.

* Tue Jun 12 2007 Götz Waschk <waschk@mandriva.org> 0.99.80-0.rc1.1mdv2008.0
+ Revision: 38104
- new version
- rediff patch 1
- update file list

* Wed May 23 2007 Götz Waschk <waschk@mandriva.org> 0.99.79-1mdv2008.0
+ Revision: 29997
- new version

* Thu May 10 2007 Götz Waschk <waschk@mandriva.org> 0.99.78-1mdv2008.0
+ Revision: 25908
- fix 64 bit build problem
- new version
- reenable flac
- patch upstream desktop file


* Thu Feb 08 2007 Götz Waschk <waschk@mandriva.org> 0.99.77-1mdv2007.0
+ Revision: 117949
- disable scopes that need gtk+ 1.2
- fix buildrequires
- new version
- disable flac plugin
- switch to gtk2.0 UI

  + Marcelo Ricardo Leitner <mrl@mandriva.com>
    - Import alsaplayer

* Wed Aug 02 2006 G�tz Waschk <waschk@mandriva.org> 0.99.76-9mdv2007.0
- xdg menu

* Fri Mar 24 2006 Götz Waschk <waschk@mandriva.org> 0.99.76-8mdk
- Rebuild
- use mkrel

* Thu May 05 2005 G�tz Waschk <waschk@mandriva.org> 0.99.76-7mdk
- fix build on x86_64

* Tue Apr 19 2005 G�tz Waschk <waschk@mandriva.org> 0.99.76-6mdk
- rebuild for new libflac

* Fri Mar 25 2005 Emmanuel Andry <eandry@free.fr> 0.99.76-5mdk
- Fixed Requires

* Fri Mar 25 2005 Emmanuel Andry <eandry@free.fr> 0.99.76-4mdk
- Added Requires plugin-ui-gtk to avoid segfault

* Tue Aug 03 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.99.76-3mdk
- rebuild for new flac

* Wed Jun 09 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.99.76-2mdk
- rebuild for new g++

