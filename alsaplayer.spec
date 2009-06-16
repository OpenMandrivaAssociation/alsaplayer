%define major       0
%define libname     %mklibname %name %major
%define libnamedev     %mklibname -d %name
%define build_flac 1

Name:		alsaplayer
Summary:	Advanced Linux Sound Architecture (ALSA) player
Version: 0.99.80
Release: %mkrel 3
Source:		ftp://ftp.alsa-project.org/pub/people/andy/%name-%version.tar.bz2
Source1:	%name-icons.tar.bz2
Patch0: alsaplayer-0.99.80-gcc4.3.patch
Patch1: alsaplayer-0.99.80-fix-str-fmt.patch
URL:		http://www.alsaplayer.org/
License:	GPLv3+
BuildRoot:	%_tmppath/%name-%version-root
Group:		Sound
BuildRequires:	libalsa-devel  
BuildRequires:	esound-devel
BuildRequires:	gtk2-devel
BuildRequires:  libmesagl-devel
BuildRequires:	libmikmod-devel 
BuildRequires:	libvorbis-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libmad-devel 
BuildRequires:	libjack-devel >= 0.70.4
BuildRequires:  libnas-devel
BuildRequires:  libsndfile-devel
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
%patch0 -p1
%patch1 -p1 -b .strfmt

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

%clean
rm -rf %buildroot

# TV: update me aka on each new upstream release, check for new plugins
%files -f %name.lang
%defattr(-, root, root)
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
%defattr(-, root, root)
%doc COPYING
%_libdir/libalsaplayer.so.0.0.2
%_libdir/libalsaplayer.so.0

%files  -n %libnamedev
%defattr(-, root, root)
%doc COPYING
%doc docs/reference/html/
%_includedir/alsaplayer/
%attr(644,root,root) %_libdir/libalsaplayer.la
%_libdir/libalsaplayer.so
%_libdir/pkgconfig/alsaplayer.pc

%if %build_flac
%files plugin-input-flac
%defattr(-, root, root)
%doc COPYING
%_libdir/%name/input/libflac_in.so
%endif

%files plugin-input-mod
%defattr(-, root, root)
%doc COPYING
%_libdir/%name/input/libmod.so

%files plugin-input-mad
%defattr(-, root, root)
%doc COPYING
%_libdir/%name/input/libmad_in.so

%files plugin-input-sndfile
%defattr(-, root, root)
%doc COPYING
%_libdir/%name/input/libsndfile_in.so

%files plugin-input-vorbis
%defattr(-, root, root)
%doc COPYING
%_libdir/%name/input/libvorbis_in.so

%files plugin-output-jack
%defattr(-, root, root)
%doc COPYING
%_libdir/%name/output/libjack_out.so

%files plugin-output-esound
%defattr(-, root, root)
%doc COPYING
%_libdir/%name/output/libesound_out.so

%files plugin-output-nas
%defattr(-, root, root)
%doc COPYING
%_libdir/%name/output/libnas_out.so

%files plugin-ui-gtk
%defattr(-, root, root)
%doc COPYING
%_libdir/%name/interface/libgtk2_interface.so

%files plugin-scopes
%defattr(-, root, root)
%doc COPYING
%_libdir/%name/scopes2
