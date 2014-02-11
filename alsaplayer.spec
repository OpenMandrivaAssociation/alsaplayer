%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Advanced Linux Sound Architecture (ALSA) player
Name:		alsaplayer
Version:	0.99.81
Release:	2
License:	GPLv3+
Group:		Sound
Url:		http://www.alsaplayer.org/
Source0:	http://www.alsaplayer.org/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
BuildRequires:	libmikmod-devel
BuildRequires:	libnas-devel
BuildRequires:	libxosd-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(esound)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(vorbis)
Requires:	%{name}-plugin-ui-gtk

%description
Advanced Linux Sound Architecture (ALSA) utils. Modularized architecture with
support for a large range of ISA and PCI cards. Fully compatible with OSS/Lite
(kernel sound drivers), but contains many enhanced features.

%files -f %{name}.lang
%doc docs/*.txt
%doc COPYING
%{_bindir}/*
%{_datadir}/applications/*.desktop
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/*/
%{_libdir}/%{name}/input/libcdda.so
%{_libdir}/%{name}/input/libwav.so
%{_libdir}/%{name}/output/libalsa_out.so
%{_libdir}/%{name}/output/libnull_out.so
%{_libdir}/%{name}/output/liboss_out.so
%{_libdir}/%{name}/interface/libdaemon_interface.so
%{_libdir}/%{name}/interface/libtext_interface.so
%{_libdir}/%{name}/interface/libxosd_interface.so
%{_libdir}/%{name}/reader/libfile.so
%{_libdir}/%{name}/reader/libhttp.so
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_mandir}/man1/%{name}.*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	AlsaPlayer shared library
Group:		System/Libraries

%description -n %{libname}
This is the shared library of AlsaPlayer.

%files -n %{libname}
%doc COPYING
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	AlsaPlayer development files
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This is the development part of the AlsaPlayer librairy.

%files  -n %{devname}
%doc COPYING
%doc docs/reference/html/
%{_includedir}/alsaplayer/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/alsaplayer.pc

#----------------------------------------------------------------------------

%package plugin-input-flac
Summary:	AlsaPlayer plugin for playing FLAC audio files
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-input-flac
This plugin enables alsaplayer to play files in the lossless audio 
compression format FLAC.

%files plugin-input-flac
%doc COPYING
%{_libdir}/%{name}/input/libflac_in.so

#----------------------------------------------------------------------------

%package plugin-input-mad
Summary:	AlsaPlayer plugin
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-input-mad
This plugin enables alsaplayer to play mpeg files though the libmad library.
It currently supports MPEG-1 and the MPEG-2  extension to Lower Sampling
Frequencies, as well as the so-called MPEG 2.5 format. All three audio layers
(Layer I, Layer II, and Layer III a.k.a. MP3) are fully implemented.

%files plugin-input-mad
%doc COPYING
%{_libdir}/%{name}/input/libmad_in.so

#----------------------------------------------------------------------------

%package plugin-input-mod
Summary:	AlsaPlayer plugin for playing MOD modules
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-input-mod
This plugin enables alsaplayer to play module music files.
Supported file formats include MOD, STM, S3M, MTM, XM, ULT, and IT.

%files plugin-input-mod
%doc COPYING
%{_libdir}/%{name}/input/libmod.so

#----------------------------------------------------------------------------

%package plugin-input-sndfile
Summary:	AlsaPlayer plugin
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-input-sndfile
This plugin enables alsaplayer to play sound files such as AIFF, AU
and WAV files through the sndfile library. It can currently read 8,
16, 24 and 32-bit PCM files as well as 32-bit floating point WAV files
and a number of compressed formats.

%files plugin-input-sndfile
%doc COPYING
%{_libdir}/%{name}/input/libsndfile_in.so

#----------------------------------------------------------------------------

%package plugin-input-vorbis
Summary:	AlsaPlayer plugin
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-input-vorbis
This plugin enables alsaplayer to play ogg vorbis music files.

%files plugin-input-vorbis
%doc COPYING
%{_libdir}/%{name}/input/libvorbis_in.so

#----------------------------------------------------------------------------

%package plugin-output-jack
Summary:	AlsaPlayer for the jack sound server
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-output-jack
This plugin enables alsaplayer to play music with the jack daemon.

%files plugin-output-jack
%doc COPYING
%{_libdir}/%{name}/output/libjack_out.so

#----------------------------------------------------------------------------

%package plugin-output-esound
Summary:	AlsaPlayer plugin
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-output-esound
This plugin enables alsaplayer to play music with the esound daemon.

%files plugin-output-esound
%doc COPYING
%{_libdir}/%{name}/output/libesound_out.so

#----------------------------------------------------------------------------

%package plugin-output-nas
Summary:	AlsaPlayer NAS output plugin
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-output-nas
This plugin enables alsaplayer to play music with the NAS daemon.

%files plugin-output-nas
%doc COPYING
%{_libdir}/%{name}/output/libnas_out.so

#----------------------------------------------------------------------------

%package plugin-ui-gtk
Summary:	AlsaPlayer UI plugin
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-ui-gtk
This plugin adds a nice graphical interface to alsaplayer.

%files plugin-ui-gtk
%doc COPYING
%{_libdir}/%{name}/interface/libgtk2_interface.so

#----------------------------------------------------------------------------

%package plugin-scopes
Summary:	AlsaPlayer graphical scopes
Group:		Sound
Requires:	%{name} = %{EVRD}

%description plugin-scopes
This plugin adds some nice graphical visualization plugins (scopes).

%files plugin-scopes
%doc COPYING
%{_libdir}/%{name}/scopes2

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%define _disable_ld_no_undefined 1
%configure2_5x \
	--enable-alsa \
	--enable-esd \
	--disable-debug \
	--enable-oggvorbis \
	--enable-gtk2
%make

%install
%makeinstall_std
#clean unpackaged files:
rm -rf %{buildroot}%{_datadir}/doc/alsaplayer

tar xfj %{SOURCE1} -C %{buildroot}%{_datadir}
# fix permissions:
chmod 755 docs/reference/html

%find_lang %{name}

