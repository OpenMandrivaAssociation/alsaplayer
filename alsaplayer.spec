%define major       0
%define libname     %mklibname %name %major
%define build_flac 1

Name:		alsaplayer
Summary:	Advanced Linux Sound Architecture (ALSA) player
Version: 0.99.78
Release: %mkrel 1
Source:		ftp://ftp.alsa-project.org/pub/people/andy/%name-%version.tar.bz2
Source1:	%name-icons.tar.bz2
Patch:		alsaplayer-0.99.75-gcc33.patch
Patch1: alsaplayer-0.99.78-desktop.patch
URL:		http://www.alsaplayer.org/
License:	GPL
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
ExcludeArch:	ppc sparc sparc64
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

%package -n %libname-devel
Summary:    AlsaPlayer devel stuff 
Group:      Development/C
Requires: %libname = %version
Provides: libalsaplayer-devel
Obsoletes: libalsaplayer-devel

%description -n %libname-devel
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
%patch
%patch1 -p1

%build
%configure2_5x --enable-alsa --enable-esd --disable-debug --enable-oggvorbis --enable-prefer-mad --disable-gtk --enable-gtk2
%make

%install
rm -rf %buildroot
 %makeinstall_std
#clean unpackaged files:
rm -rf %buildroot%_datadir/doc/alsaplayer
rm -rf %buildroot%_libdir/%name/*/*.la

mkdir -p $RPM_BUILD_ROOT{%_menudir,%_datadir}
cat << EOF > $RPM_BUILD_ROOT%_menudir/%name
?package(%name):\
needs="x11"\
longtitle="The Alsa Player" \
section="Multimedia/Sound"\
title="Alsa Player"\
command="%{name}"\
icon="%name.png" xdg="true"
EOF

tar xfj %SOURCE1 -C %buildroot/%_datadir
# fix permissions:
chmod 755 docs/reference/html

%post
%update_menus

%postun
%clean_menus

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf %buildroot

# TV: update me aka on each new upstream release, check for new plugins
%files
%defattr(-, root, root)
%doc docs/*.txt
%doc COPYING
%_datadir/applications/*.desktop
%_menudir/%name
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

%files  -n %libname-devel
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
%_libdir/%name/scopes/liboglspectrum.so
%if 0
#gw these need gtk+ 1.2
%_libdir/%name/scopes/libblurscope.so
%_libdir/%name/scopes/liblogbarfft.so
%_libdir/%name/scopes/libsynaescope.so
%_libdir/%name/scopes/liblevelmeter.so
%_libdir/%name/scopes/libmonoscope.so
%_libdir/%name/scopes/libspacescope.so
%endif


