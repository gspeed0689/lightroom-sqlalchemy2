CREATE INDEX index_Adobe_AdditionalMetadata_imageAndStatus ON Adobe_AdditionalMetadata( image, externalXmpIsDirty );
CREATE INDEX index_Adobe_faceProperties_face ON Adobe_faceProperties( face );
CREATE INDEX index_Adobe_imageDevelopBeforeSettings_developSettings ON Adobe_imageDevelopBeforeSettings( developSettings );
CREATE INDEX index_Adobe_imageDevelopSettings_image ON Adobe_imageDevelopSettings( image );
CREATE INDEX index_Adobe_imageDevelopSettings_digest ON Adobe_imageDevelopSettings( digest );
CREATE INDEX index_Adobe_imageProofSettings_image ON Adobe_imageProofSettings( image );
CREATE INDEX index_Adobe_imageProperties_image ON Adobe_imageProperties( image );
CREATE INDEX index_Adobe_images_rootFile ON Adobe_images( rootFile );
CREATE INDEX index_Adobe_images_ratingAndCaptureTime ON Adobe_images( rating, captureTime );
CREATE INDEX index_Adobe_images_originalRootEntity ON Adobe_images( originalRootEntity );
CREATE INDEX index_Adobe_images_masterImage ON Adobe_images( masterImage );
CREATE INDEX index_Adobe_images_captureTime ON Adobe_images( captureTime );
CREATE INDEX index_Adobe_libraryImageDevelopHistoryStep_imageDateCreated ON Adobe_libraryImageDevelopHistoryStep( image, dateCreated );
CREATE INDEX index_Adobe_libraryImageDevelopSnapshot_image ON Adobe_libraryImageDevelopSnapshot( image );
CREATE INDEX index_Adobe_libraryImageFaceProcessHistory_image ON Adobe_libraryImageFaceProcessHistory( image );
CREATE INDEX index_Adobe_namedIdentityPlate_description ON Adobe_namedIdentityPlate( description );
CREATE INDEX index_Adobe_namedIdentityPlate_identityPlateHash ON Adobe_namedIdentityPlate( identityPlateHash );
CREATE INDEX index_Adobe_variables_name ON Adobe_variables( name );
CREATE UNIQUE INDEX index_AgDeletedOzAlbumAssetIds_primaryKey ON
	AgDeletedOzAlbumAssetIds( ozCatalogId, ozAlbumAssetId );
CREATE INDEX index_AgDeletedOzAlbumAssetIds_changeCounter ON
	AgDeletedOzAlbumAssetIds( changeCounter, ozCatalogId, ozAlbumAssetId );
CREATE UNIQUE INDEX index_AgDeletedOzAlbumIds_primaryKey ON
	AgDeletedOzAlbumIds( ozCatalogId, ozAlbumId );
CREATE INDEX index_AgDeletedOzAlbumIds_changeCounter ON
	AgDeletedOzAlbumIds( changeCounter, ozCatalogId, ozAlbumId );
CREATE UNIQUE INDEX index_AgDeletedOzAssetIds_primaryKey ON
	AgDeletedOzAssetIds( ozCatalogId, ozAssetId );
CREATE INDEX index_AgDeletedOzAssetIds_changeCounter ON
	AgDeletedOzAssetIds( changeCounter, ozCatalogId, ozAssetId );
CREATE UNIQUE INDEX index_AgDeletedOzSpaceIds_primaryKey ON
	AgDeletedOzSpaceIds( ozCatalogId, ozSpaceId );
CREATE INDEX index_AgDevelopAdditionalMetadata_image ON AgDevelopAdditionalMetadata( image );
CREATE INDEX index_AgDNGProxyInfo_statusDateTimeForUUID ON AgDNGProxyInfo( status, statusDateTime, fileUUID );
CREATE INDEX index_AgDNGProxyInfo_uuidStatusDateTime ON AgDNGProxyInfo( fileUUID, status, statusDateTime );
CREATE INDEX index_AgDNGProxyInfoUpdater_taskIDCluster ON AgDNGProxyInfoUpdater( taskID, whenPosted, taskStatus );
CREATE INDEX index_AgDNGProxyInfoUpdater_statusCluster ON AgDNGProxyInfoUpdater( taskStatus, whenPosted, taskID );
CREATE INDEX index_AgFolderContent_owningModule ON AgFolderContent( owningModule );
CREATE INDEX index_AgFolderContent_containingFolder ON AgFolderContent( containingFolder );
CREATE INDEX index_AgHarvestedDNGMetadata_byHasLossyCompression ON AgHarvestedDNGMetadata( hasLossyCompression, image, isDNG, hasFastLoadData, isReducedResolution, isPano, isHDR );
CREATE INDEX index_AgHarvestedDNGMetadata_byIsHDR ON AgHarvestedDNGMetadata( isHDR, image, isDNG, hasFastLoadData, hasLossyCompression, isReducedResolution, isPano );
CREATE INDEX index_AgHarvestedDNGMetadata_byIsPano ON AgHarvestedDNGMetadata( isPano, image, isDNG, hasFastLoadData, hasLossyCompression, isReducedResolution, isHDR );
CREATE INDEX index_AgHarvestedDNGMetadata_byHasFastLoadData ON AgHarvestedDNGMetadata( hasFastLoadData, image, isDNG, hasLossyCompression, isReducedResolution, isPano, isHDR );
CREATE INDEX index_AgHarvestedDNGMetadata_byImage ON AgHarvestedDNGMetadata( image, isDNG, hasFastLoadData, hasLossyCompression, isReducedResolution, isPano, isHDR );
CREATE INDEX index_AgHarvestedDNGMetadata_byIsDNG ON AgHarvestedDNGMetadata( isDNG, image, hasFastLoadData, hasLossyCompression, isReducedResolution, isPano, isHDR );
CREATE INDEX index_AgHarvestedDNGMetadata_byIsReducedResolution ON AgHarvestedDNGMetadata( isReducedResolution, image, isDNG, hasFastLoadData, hasLossyCompression, isPano, isHDR );
CREATE INDEX index_AgHarvestedExifMetadata_cameraSNRef ON AgHarvestedExifMetadata( cameraSNRef );
CREATE INDEX index_AgHarvestedExifMetadata_lensRef ON AgHarvestedExifMetadata( lensRef );
CREATE INDEX index_AgHarvestedExifMetadata_focalLength ON AgHarvestedExifMetadata( focalLength );
CREATE INDEX index_AgHarvestedExifMetadata_flashFired ON AgHarvestedExifMetadata( flashFired );
CREATE INDEX index_AgHarvestedExifMetadata_shutterSpeed ON AgHarvestedExifMetadata( shutterSpeed );
CREATE INDEX index_AgHarvestedExifMetadata_cameraModelRef ON AgHarvestedExifMetadata( cameraModelRef );
CREATE INDEX index_AgHarvestedExifMetadata_isoSpeedRating ON AgHarvestedExifMetadata( isoSpeedRating );
CREATE INDEX index_AgHarvestedExifMetadata_image ON AgHarvestedExifMetadata( image );
CREATE INDEX index_AgHarvestedExifMetadata_date ON AgHarvestedExifMetadata( dateYear, dateMonth, dateDay, image );
CREATE INDEX index_AgHarvestedExifMetadata_gpsCluster ON AgHarvestedExifMetadata( hasGPS, gpsLatitude, gpsLongitude, image );
CREATE INDEX index_AgHarvestedExifMetadata_aperture ON AgHarvestedExifMetadata( aperture );
CREATE INDEX index_AgHarvestedIptcMetadata_isoCountryCodeRef ON AgHarvestedIptcMetadata( isoCountryCodeRef );
CREATE INDEX index_AgHarvestedIptcMetadata_stateRef ON AgHarvestedIptcMetadata( stateRef );
CREATE INDEX index_AgHarvestedIptcMetadata_locationDataOrigination ON AgHarvestedIptcMetadata( locationDataOrigination );
CREATE INDEX index_AgHarvestedIptcMetadata_image ON AgHarvestedIptcMetadata( image );
CREATE INDEX index_AgHarvestedIptcMetadata_jobIdentifierRef ON AgHarvestedIptcMetadata( jobIdentifierRef );
CREATE INDEX index_AgHarvestedIptcMetadata_cityRef ON AgHarvestedIptcMetadata( cityRef );
CREATE INDEX index_AgHarvestedIptcMetadata_creatorRef ON AgHarvestedIptcMetadata( creatorRef );
CREATE INDEX index_AgHarvestedIptcMetadata_countryRef ON AgHarvestedIptcMetadata( countryRef );
CREATE INDEX index_AgHarvestedIptcMetadata_copyrightState ON AgHarvestedIptcMetadata( copyrightState );
CREATE INDEX index_AgHarvestedIptcMetadata_locationRef ON AgHarvestedIptcMetadata( locationRef );
CREATE INDEX index_AgHarvestedMetadataWorklist_taskIDCluster ON AgHarvestedMetadataWorklist( taskID, whenPosted, taskStatus );
CREATE INDEX index_AgHarvestedMetadataWorklist_statusCluster ON AgHarvestedMetadataWorklist( taskStatus, whenPosted, taskID );
CREATE INDEX index_AgInternedExifCameraModel_value ON AgInternedExifCameraModel( value );
CREATE INDEX index_AgInternedExifCameraModel_searchIndex ON AgInternedExifCameraModel( searchIndex );
CREATE INDEX index_AgInternedExifCameraSN_value ON AgInternedExifCameraSN( value );
CREATE INDEX index_AgInternedExifCameraSN_searchIndex ON AgInternedExifCameraSN( searchIndex );
CREATE INDEX index_AgInternedExifLens_searchIndex ON AgInternedExifLens( searchIndex );
CREATE INDEX index_AgInternedExifLens_value ON AgInternedExifLens( value );
CREATE INDEX index_AgInternedIptcCity_searchIndex ON AgInternedIptcCity( searchIndex );
CREATE INDEX index_AgInternedIptcCity_value ON AgInternedIptcCity( value );
CREATE INDEX index_AgInternedIptcCountry_value ON AgInternedIptcCountry( value );
CREATE INDEX index_AgInternedIptcCountry_searchIndex ON AgInternedIptcCountry( searchIndex );
CREATE INDEX index_AgInternedIptcCreator_value ON AgInternedIptcCreator( value );
CREATE INDEX index_AgInternedIptcCreator_searchIndex ON AgInternedIptcCreator( searchIndex );
CREATE INDEX index_AgInternedIptcIsoCountryCode_value ON AgInternedIptcIsoCountryCode( value );
CREATE INDEX index_AgInternedIptcIsoCountryCode_searchIndex ON AgInternedIptcIsoCountryCode( searchIndex );
CREATE INDEX index_AgInternedIptcJobIdentifier_value ON AgInternedIptcJobIdentifier( value );
CREATE INDEX index_AgInternedIptcJobIdentifier_searchIndex ON AgInternedIptcJobIdentifier( searchIndex );
CREATE INDEX index_AgInternedIptcLocation_value ON AgInternedIptcLocation( value );
CREATE INDEX index_AgInternedIptcLocation_searchIndex ON AgInternedIptcLocation( searchIndex );
CREATE INDEX index_AgInternedIptcState_searchIndex ON AgInternedIptcState( searchIndex );
CREATE INDEX index_AgInternedIptcState_value ON AgInternedIptcState( value );
CREATE INDEX index_AgLibraryCollection_parentAndName ON AgLibraryCollection( parent, name );
CREATE INDEX index_AgLibraryCollection_genealogy ON AgLibraryCollection( genealogy );
CREATE INDEX index_AgLibraryCollectionChangeCounter_changeCounter ON
	AgLibraryCollectionChangeCounter( changeCounter, collection );
CREATE INDEX index_AgLibraryCollectionContent_collection ON AgLibraryCollectionContent( collection );
CREATE INDEX index_AgLibraryCollectionContent_owningModule ON AgLibraryCollectionContent( owningModule );
CREATE INDEX index_AgLibraryCollectionImage_collection ON AgLibraryCollectionImage( collection );
CREATE INDEX index_AgLibraryCollectionImage_imageCollection ON AgLibraryCollectionImage( image, collection );
CREATE INDEX index_AgLibraryCollectionImageChangeCounter_changeCounter ON
	AgLibraryCollectionImageChangeCounter( changeCounter, collectionImage,
											collection, image );
CREATE UNIQUE INDEX index_AgLibraryCollectionImageOzAlbumAssetIds_primaryKey ON
	AgLibraryCollectionImageOzAlbumAssetIds( collectionImage, ozCatalogId,
												collection, image );
CREATE INDEX index_AgLibraryCollectionImageOzAlbumAssetIds_collectionFromAlbumAssetIdLookup ON
	AgLibraryCollectionImageOzAlbumAssetIds( ozAlbumAssetId, ozCatalogId,
												collectionImage, collection,
												image );
CREATE INDEX index_AgLibraryCollectionImageOzAlbumAssetIds_collectionAlbumAssetsLookup ON
	AgLibraryCollectionImageOzAlbumAssetIds( collection, ozCatalogId );
CREATE INDEX index_AgLibraryCollectionImageOzAlbumAssetIds_imageAlbumAssetsLookup ON
	AgLibraryCollectionImageOzAlbumAssetIds( image, ozCatalogId );
CREATE INDEX index_AgLibraryCollectionLabel_labelIndex ON AgLibraryCollectionLabel( label );
CREATE INDEX index_AgLibraryCollectionLabel_collectiondex ON AgLibraryCollectionLabel( collection );
CREATE UNIQUE INDEX index_AgLibraryCollectionLabel_collectionLabelIndex ON AgLibraryCollectionLabel( collection, label );
CREATE UNIQUE INDEX index_AgLibraryCollectionOzAlbumIds_primaryKey ON
	AgLibraryCollectionOzAlbumIds( collection, ozCatalogId );
CREATE INDEX index_AgLibraryCollectionOzAlbumIds_collectionFromAlbumIdLookup ON
	AgLibraryCollectionOzAlbumIds( ozAlbumId, ozCatalogId, collection );
CREATE INDEX index_AgLibraryCollectionOzAlbumIds_catalogAlbumsLookup ON
	AgLibraryCollectionOzAlbumIds( ozCatalogId, ozAlbumId, collection );
CREATE INDEX index_AgLibraryCollectionStack_stacksForCollection ON AgLibraryCollectionStack( collection, collapsed );
CREATE INDEX index_AgLibraryCollectionStackData ON AgLibraryCollectionStackData( stack, collection, stackCount, stackParent );
CREATE INDEX index_AgLibraryCollectionStackImage_stack ON AgLibraryCollectionStackImage( stack );
CREATE INDEX index_AgLibraryCollectionStackImage_orderByCollapseThenStackThenPosition ON AgLibraryCollectionStackImage( collection, collapsed, stack, position, image );
CREATE INDEX index_AgLibraryCollectionStackImage_orderByStackThenPosition ON AgLibraryCollectionStackImage( collection, stack, position, image, collapsed );
CREATE INDEX index_AgLibraryCollectionStackImage_image ON AgLibraryCollectionStackImage( image );
CREATE INDEX index_AgLibraryCollectionStackImage_getStackFromImage ON AgLibraryCollectionStackImage( collection, image, stack, position, collapsed );
CREATE INDEX index_AgLibraryCollectionStackImage_orderByPositionThenStack ON AgLibraryCollectionStackImage( collection, position, stack, image, collapsed );
CREATE UNIQUE INDEX index_AgLibraryCollectionSyncedAlbumData_primaryKey ON
	AgLibraryCollectionSyncedAlbumData( collection, payloadKey );
CREATE UNIQUE INDEX index_AgLibraryCollectionTrackedAssets_primaryKey ON
	AgLibraryCollectionTrackedAssets( collection, ozCatalogId );
CREATE INDEX index_AgLibraryCollectionTrackedAssets_byOzCatalogId ON
	AgLibraryCollectionTrackedAssets( ozCatalogId, collection );
CREATE INDEX index_AgLibraryFace_cluster ON AgLibraryFace( cluster );
CREATE INDEX index_AgLibraryFace_image ON AgLibraryFace( image );
CREATE INDEX index_AgLibraryFaceCluster_keyFace ON AgLibraryFaceCluster( keyFace );
CREATE INDEX index_AgLibraryFaceData_face ON AgLibraryFaceData( face );
CREATE UNIQUE INDEX index_AgLibraryFile_nameAndFolder ON AgLibraryFile( lc_idx_filename, folder );
CREATE INDEX index_AgLibraryFile_folder ON AgLibraryFile( folder );
CREATE INDEX index_AgLibraryFile_importHash ON AgLibraryFile( importHash );
CREATE INDEX index_AgLibraryFileAssetMetadata_sha256ToFileId  ON
	AgLibraryFileAssetMetadata( sha256, fileSize );
CREATE UNIQUE INDEX index_AgLibraryFolder_rootFolderAndPath ON AgLibraryFolder( rootFolder, pathFromRoot );
CREATE INDEX index_AgLibraryFolder_parentId ON AgLibraryFolder( parentId );
CREATE UNIQUE INDEX index_AgLibraryFolderFavorite_folderFavoriteIndex ON AgLibraryFolderFavorite( folder, favorite );
CREATE INDEX index_AgLibraryFolderFavorite_favoriteIndex ON AgLibraryFolderFavorite( favorite );
CREATE INDEX index_AgLibraryFolderFavorite_folderIndex ON AgLibraryFolderFavorite( folder );
CREATE INDEX index_AgLibraryFolderLabel_labelIndex ON AgLibraryFolderLabel( label );
CREATE INDEX index_AgLibraryFolderLabel_folderdex ON AgLibraryFolderLabel( folder );
CREATE UNIQUE INDEX index_AgLibraryFolderLabel_folderLabelIndex ON AgLibraryFolderLabel( folder, label );
CREATE INDEX index_AgLibraryFolderStack_collapsed ON AgLibraryFolderStack( collapsed );
CREATE INDEX index_AgLibraryFolderStackData ON AgLibraryFolderStackData( stack, stackCount, stackParent );
CREATE INDEX index_AgLibraryFolderStackImage_orderByPositionThenStack ON AgLibraryFolderStackImage( position, stack, image, collapsed );
CREATE INDEX index_AgLibraryFolderStackImage_orderByStackThenPosition ON AgLibraryFolderStackImage( stack, position, image, collapsed );
CREATE INDEX index_AgLibraryFolderStackImage_getStackFromImage ON AgLibraryFolderStackImage( image, stack, position, collapsed );
CREATE INDEX index_AgLibraryFolderStackImage_orderByCollapseThenStackThenPosition ON AgLibraryFolderStackImage( collapsed, stack, position, image );
CREATE INDEX index_AgLibraryImageChangeCounter_changeCounter ON
	AgLibraryImageChangeCounter( changeCounter, image );
CREATE UNIQUE INDEX index_AgLibraryImageOzAssetIds_primaryKey ON
	AgLibraryImageOzAssetIds( image, ozCatalogId );
CREATE INDEX index_AgLibraryImageOzAssetIds_imageFromAssetIdLookup ON
	AgLibraryImageOzAssetIds( ozAssetId, ozCatalogId, image, ownedByCatalog );
CREATE INDEX index_AgLibraryImageSaveXMP_taskIDCluster ON AgLibraryImageSaveXMP( taskID, whenPosted, taskStatus );
CREATE INDEX index_AgLibraryImageSaveXMP_statusCluster ON AgLibraryImageSaveXMP( taskStatus, whenPosted, taskID );
CREATE INDEX index_AgLibraryImageSearchData_image ON AgLibraryImageSearchData( image );
CREATE UNIQUE INDEX index_AgLibraryImageSyncedAssetData_primaryKey ON
	AgLibraryImageSyncedAssetData( image, payloadKey );
CREATE INDEX index_AgLibraryImageXMPUpdater_statusCluster ON AgLibraryImageXMPUpdater( taskStatus, whenPosted, taskID );
CREATE INDEX index_AgLibraryImageXMPUpdater_taskIDCluster ON AgLibraryImageXMPUpdater( taskID, whenPosted, taskStatus );
CREATE INDEX index_AgLibraryImportImage_import ON AgLibraryImportImage( import );
CREATE UNIQUE INDEX index_AgLibraryImportImage_imageAndImport ON AgLibraryImportImage( image, import );
CREATE INDEX index_AgLibraryIPTC_image ON AgLibraryIPTC( image );
CREATE INDEX index_AgLibraryKeyword_genealogy ON AgLibraryKeyword( genealogy );
CREATE UNIQUE INDEX index_AgLibraryKeyword_parentAndLcName ON AgLibraryKeyword( parent, lc_name );
CREATE INDEX index_AgLibraryKeywordCooccurrence_tag1Search ON AgLibraryKeywordCooccurrence( tag1, value, tag2 );
CREATE INDEX index_AgLibraryKeywordCooccurrence_valueIndex ON AgLibraryKeywordCooccurrence( value );
CREATE INDEX index_AgLibraryKeywordCooccurrence_tagsLookup ON AgLibraryKeywordCooccurrence( tag1, tag2 );
CREATE INDEX index_AgLibraryKeywordFace_face ON AgLibraryKeywordFace( face );
CREATE INDEX index_AgLibraryKeywordFace_tag ON AgLibraryKeywordFace( tag );
CREATE INDEX index_AgLibraryKeywordImage_tag ON AgLibraryKeywordImage( tag );
CREATE INDEX index_AgLibraryKeywordImage_image ON AgLibraryKeywordImage( image );
CREATE INDEX index_AgLibraryKeywordPopularity_popularity ON AgLibraryKeywordPopularity( popularity );
CREATE INDEX index_AgLibraryKeywordSynonym_lc_name ON AgLibraryKeywordSynonym( lc_name );
CREATE INDEX index_AgLibraryKeywordSynonym_keyword ON AgLibraryKeywordSynonym( keyword );
CREATE UNIQUE INDEX index_AgLibraryOzCommentIds_primaryKey ON
	AgLibraryOzCommentIds( ozCatalogId, ozCommentId );
CREATE INDEX index_AgLibraryOzCommentIds_byAsset ON
	AgLibraryOzCommentIds( ozCatalogId, ozSpaceId, ozAssetId );
CREATE INDEX index_AgLibraryOzCommentIds_bySpace ON 
	AgLibraryOzCommentIds( ozCatalogId, ozSpaceId );
CREATE UNIQUE INDEX index_AgLibraryOzFavoriteIds_primaryKey ON
	AgLibraryOzFavoriteIds( ozCatalogId, ozFavoriteId );
CREATE INDEX index_AgLibraryOzFavoriteIds_byAsset ON
	AgLibraryOzFavoriteIds( ozCatalogId, ozSpaceId, ozAssetId );
CREATE INDEX index_AgLibraryOzFavoriteIds_bySpace ON 
	AgLibraryOzFavoriteIds( ozCatalogId, ozSpaceId );
CREATE INDEX index_AgLibraryOzFeedbackInfo_lastFeedbackTime ON AgLibraryOzFeedbackInfo( lastFeedbackTime );
CREATE UNIQUE INDEX index_AgLibraryOzFeedbackInfo_assetAndSpaceAndCatalog ON AgLibraryOzFeedbackInfo( ozAssetId, ozSpaceId, ozCatalogId );
CREATE INDEX index_AgLibraryPublishedCollection_parentAndName ON AgLibraryPublishedCollection( parent, name );
CREATE INDEX index_AgLibraryPublishedCollection_genealogy ON AgLibraryPublishedCollection( genealogy );
CREATE INDEX index_AgLibraryPublishedCollectionContent_collection ON AgLibraryPublishedCollectionContent( collection );
CREATE INDEX index_AgLibraryPublishedCollectionContent_owningModule ON AgLibraryPublishedCollectionContent( owningModule );
CREATE INDEX index_AgLibraryPublishedCollectionImage_imageCollection ON AgLibraryPublishedCollectionImage( image, collection );
CREATE INDEX index_AgLibraryPublishedCollectionImage_collection ON AgLibraryPublishedCollectionImage( collection );
CREATE INDEX index_AgLibraryPublishedCollectionLabel_collectiondex ON AgLibraryPublishedCollectionLabel( collection );
CREATE UNIQUE INDEX index_AgLibraryPublishedCollectionLabel_collectionLabelIndex ON AgLibraryPublishedCollectionLabel( collection, label );
CREATE INDEX index_AgLibraryPublishedCollectionLabel_labelIndex ON AgLibraryPublishedCollectionLabel( label );
CREATE INDEX index_AgMetadataSearchIndex_image ON AgMetadataSearchIndex( image );
CREATE INDEX index_AgMRULists_listID ON AgMRULists( listID );
CREATE INDEX index_AgOutputImageAsset_image ON AgOutputImageAsset( image );
CREATE INDEX index_AgOutputImageAsset_findByCollectionGroupByImage ON AgOutputImageAsset( moduleId, collection, image, assetId );
CREATE INDEX index_AgOutputImageAsset_findByCollectionImage ON AgOutputImageAsset( collection, image, moduleId, assetId );
CREATE INDEX index_AgOzAuxBinaryMetadata_byAsset  ON
	AgOzAuxBinaryMetadata( ozAssetId );
CREATE INDEX index_AgOzCorruptedAuxIds_byAsset  ON
	AgOzCorruptedAuxIds( ozAssetId );
CREATE UNIQUE INDEX index_AgOzSpaceAlbumIds_primaryKey ON
	AgOzSpaceAlbumIds( ozSpaceAlbumId );
CREATE INDEX index_AgOzSpaceAlbumIds_bySpaceId ON
	AgOzSpaceAlbumIds( ozSpaceId, ozCatalogId );
CREATE INDEX index_AgOzSpaceAlbumIds_byAlbumId ON
	AgOzSpaceAlbumIds( ozAlbumId, ozCatalogId );
CREATE UNIQUE INDEX index_AgOzSpaceIds_primaryKey ON
	AgOzSpaceIds( ozCatalogId, ozSpaceId );
CREATE UNIQUE INDEX index_AgPendingOzAlbumAssetIds_primaryKey ON
	AgPendingOzAlbumAssetIds( ozCatalogId, ozAlbumAssetId, ozAssetId, ozAlbumId );
CREATE INDEX index_AgPendingOzAlbumAssetIds_byAlbumAssetId ON
	AgPendingOzAlbumAssetIds( ozAlbumAssetId, ozAssetId, ozCatalogId, ozAlbumId );
CREATE INDEX index_AgPendingOzAlbumAssetIds_byAssetId ON
	AgPendingOzAlbumAssetIds( ozAssetId, ozCatalogId, ozAlbumAssetId, ozAlbumId );
CREATE INDEX index_AgPendingOzAlbumAssetIds_byAlbumId ON
	AgPendingOzAlbumAssetIds( ozAlbumId, ozCatalogId, ozAlbumAssetId, ozAssetId );
CREATE UNIQUE INDEX index_AgPendingOzAssetBinaryDownloads_primaryKey ON
	AgPendingOzAssetBinaryDownloads( ozAssetId, ozCatalogId );
CREATE INDEX index_AgPendingOzAssetBinaryDownloads_catalogIdOrdering ON
	AgPendingOzAssetBinaryDownloads( ozCatalogId, whenQueued, state, ozAssetId, path );
CREATE INDEX index_AgPendingOzAssetBinaryDownloads_stateSearches ON
	AgPendingOzAssetBinaryDownloads( state, ozCatalogId, whenQueued, ozAssetId );
CREATE UNIQUE INDEX index_AgPendingOzAssets_primaryKey ON
	AgPendingOzAssets( ozAssetId, ozCatalogId );
CREATE INDEX index_AgPendingOzAssets_stateSearches ON
	AgPendingOzAssets( state, ozCatalogId, ozAssetId );
CREATE INDEX index_AgPhotoComment_remotePhoto ON AgPhotoComment( remotePhoto );
CREATE INDEX index_AgPhotoComment_photo ON AgPhotoComment( photo );
CREATE INDEX index_AgPhotoComment_remoteId ON AgPhotoComment( remoteId );
CREATE INDEX index_AgPhotoProperty_propertySpec ON AgPhotoProperty( propertySpec );
CREATE UNIQUE INDEX index_AgPhotoProperty_pluginKey ON AgPhotoProperty( photo, propertySpec );
CREATE INDEX index_AgPhotoPropertyArrayElement_propertySpec ON AgPhotoPropertyArrayElement( propertySpec );
CREATE UNIQUE INDEX index_AgPhotoPropertyArrayElement_pluginKey ON AgPhotoPropertyArrayElement( photo, propertySpec, arrayIndex );
CREATE UNIQUE INDEX index_AgPhotoPropertySpec_pluginKey ON AgPhotoPropertySpec( sourcePlugin, key, pluginVersion );
CREATE INDEX index_AgPublishListenerWorklist_statusCluster ON AgPublishListenerWorklist( taskStatus, whenPosted, taskID );
CREATE INDEX index_AgPublishListenerWorklist_taskIDCluster ON AgPublishListenerWorklist( taskID, whenPosted, taskStatus );
CREATE INDEX index_AgRemotePhoto_collectionNeedsUpdating ON AgRemotePhoto( collection, photoNeedsUpdating );
CREATE UNIQUE INDEX index_AgRemotePhoto_collectionRemoteId ON AgRemotePhoto( collection, remoteId );
CREATE INDEX index_AgRemotePhoto_photo ON AgRemotePhoto( photo );
CREATE UNIQUE INDEX index_AgRemotePhoto_collectionPhoto ON AgRemotePhoto( collection, photo );
CREATE INDEX index_AgSearchablePhotoProperty_propertyValue_lc ON AgSearchablePhotoProperty( propertySpec, lc_idx_internalValue );
CREATE INDEX index_AgSearchablePhotoProperty_lc_idx_internalValue ON AgSearchablePhotoProperty( lc_idx_internalValue );
CREATE UNIQUE INDEX index_AgSearchablePhotoProperty_pluginKey ON AgSearchablePhotoProperty( photo, propertySpec );
CREATE INDEX index_AgSearchablePhotoProperty_propertyValue ON AgSearchablePhotoProperty( propertySpec, internalValue );
CREATE INDEX index_AgSearchablePhotoPropertyArrayElement_propertyValue ON AgSearchablePhotoPropertyArrayElement( propertySpec, internalValue );
CREATE UNIQUE INDEX index_AgSearchablePhotoPropertyArrayElement_pluginKey ON AgSearchablePhotoPropertyArrayElement( photo, propertySpec, arrayIndex );
CREATE INDEX index_AgSearchablePhotoPropertyArrayElement_lc_idx_internalValue ON AgSearchablePhotoPropertyArrayElement( lc_idx_internalValue );
CREATE INDEX index_AgSearchablePhotoPropertyArrayElement_propertyValue_lc ON AgSearchablePhotoPropertyArrayElement( propertySpec, lc_idx_internalValue );
CREATE INDEX index_AgSourceColorProfileConstants_image ON AgSourceColorProfileConstants( image );
CREATE INDEX index_AgSourceColorProfileConstants_imageSourceColorProfileName ON AgSourceColorProfileConstants( profileName, image );
CREATE UNIQUE INDEX index_AgSpecialSourceContent_sourceModule ON AgSpecialSourceContent( source, owningModule );
CREATE INDEX index_AgSpecialSourceContent_owningModule ON AgSpecialSourceContent( owningModule );
CREATE INDEX index_AgVideoInfo_image ON AgVideoInfo( image );